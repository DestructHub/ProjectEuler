defmodule Settings do
  def start_link do
    Agent.start_link &initial_state/0, name: __MODULE__
  end

  defp initial_state do
    env = System.get_env("STATS_POOL_SIZE")
    parsed = env && case Integer.parse(env) do
      {int, _} -> int
      :error -> false
    end
    pool_size = parsed || 2 * :erlang.system_info(:schedulers_online)

    %{pool_size: pool_size}
  end

  def get(key) do
    Agent.get __MODULE__, &(&1[key])
  end

  def set(key, value) do
    Agent.update __MODULE__, & Map.put(&1, key, value)
  end
end

defmodule CLI do
  @parse_opts [
    strict: [
      help: :boolean,
      search: [:string, :keep],
      pool_size: :integer,
      all: :boolean
    ],

    aliases: [
      h: :help,
      s: :search,
      p: :pool_size,
      a: :all
    ]
  ]

  def run do
    OptionParser.parse(System.argv(), @parse_opts)
    |> process
  end

  def process({[help: true], _, _}) do
    help()
  end

  def process({parsed, _, _}) do
    all_languages? = Keyword.get parsed, :all, false
    languages = Keyword.get_values(parsed, :search)
    pool_size = Keyword.get parsed, :pool_size, Settings.get(:pool_size)

    Settings.set(:pool_size, pool_size)

    if not all_languages? and Enum.empty?(languages) do
      help()
    else
      languages
      |> Enum.map(& String.downcase(&1))
      |> Producer.start_link(all_languages?)

      Consumer.start_link()
      Renderer.start_link()
      Manager.start_link()
      Manager.start_workers()
    end
  end

  defp help do
    IO.puts """
    TODO: help
    """

    System.halt(0)
  end
end

defmodule Producer do
  use GenServer

  def start_link(languages, all_languages?) do
    GenServer.start_link __MODULE__, problems(languages, all_languages?), name: __MODULE__
  end

  def init(problems) do
    {:ok, problems}
  end

  def pop do
    GenServer.call __MODULE__, :pop
  end

  def handle_call(:pop, _from, [h | t]) do
    {:reply, {:ok, h}, t}
  end
  def handle_call(:pop, _from, []) do
    {:reply, :error, []}
  end

  defp problems(languages, all_languages?) do
    language_filter = if all_languages? do
      fn _ -> true end
    else
      fn language -> Enum.member?(languages, String.downcase(language)) end
    end

    File.ls!(".")
    |> Enum.filter(& Regex.match?(~r/Problem\d{1,3}/, &1))
    |> Enum.flat_map(fn problem ->
      File.ls!(problem)
      |> Enum.filter(& problem |> Path.join(&1) |> File.dir?)
      |> Enum.filter(language_filter)
      |> Enum.map(fn lang ->
        File.ls!(Path.join(problem, lang))
        |> Enum.reject(& Regex.match?(~r/(.+)\.out$/, &1))
        |> Enum.filter(& Regex.match?(~r/^solution_\d+/, &1))
        |> Enum.map(fn solution ->
          {lang, solution}
        end)
      end)
      |> Enum.flat_map(fn solutions ->
        solutions
        |> Enum.map(fn {lang, solution} ->
          {problem, lang, solution}
        end)
      end)
    end)
  end
end

defmodule Manager do
  use GenServer

  def start_link do
    workers = span_workers(Settings.get(:pool_size))
    GenServer.start_link __MODULE__, workers, name: __MODULE__
  end

  def init(workers) do
    state =
      workers
      |> Enum.reduce({[], %{}}, fn ({id, worker}, {xs, map}) ->
        {[id | xs], Map.put(map, id, worker)}
      end)

    {:ok, state}
  end

  def start_workers do
    :ok = GenServer.cast __MODULE__, :start_workers
  end

  def next do
    :ok = GenServer.cast __MODULE__, :next
  end

  def finished(id, solution, time) do
    :ok = GenServer.cast __MODULE__, {:finished, id, solution, time}
  end

  def handle_cast(:start_workers, {workers, _} = state) do
    for _ <- workers, do: Manager.next()
    {:noreply, state}
  end
  def handle_cast(:next, {[id | available], workers}) do
    worker = workers[id]

    case Producer.pop() do
      {:ok, {problem, _, file} = solution} ->
        Worker.run(worker, solution)
        Renderer.set_label(id, problem <> "/" <> file)

        {:noreply, {available, workers}}
      _ ->
        Renderer.set_label(id, "Finishing last jobs")

        workers = Map.delete(workers, id)

        if workers == %{} do
          Consumer.output()
        end

        {:noreply, {available, workers}}
    end
  end
  def handle_cast({:finished, id, solution, time}, {available, workers}) do
    Renderer.delete_label(id)
    Consumer.consume(solution, time)
    next()
    {:noreply, {[id | available], workers}}
  end

  defp span_workers(n) do
    for id <- 1..n do
      {:ok, pid} = Worker.start_link(id)
      {id, pid}
    end
  end
end

defmodule Worker do
  use GenServer

  def start_link(id) do
    GenServer.start_link __MODULE__, id
  end

  def init(id) do
    {:ok, id}
  end

  def run(worker, solution) do
    :ok = GenServer.cast worker, {:run, solution}
  end

  def handle_cast({:run, solution}, id) do
    {time, _} =
      :timer.tc(fn ->
        Runner.run(solution)
      end)

    Manager.finished(id, solution, time)

    {:noreply, id}
  end
end

defmodule Runner do
  @build_machine %{
    "Python" => %{
      cmd: "python3",
      builder: :execute
    },

    "Elixir" => %{
      cmd: "elixir",
      builder: :execute
    },

    "Go" => %{
      cmd: "go run",
      builder: :execute
    },

    "Clojure" => %{
      cmd: "clojure",
      builder: :execute
    },

    "CommonLisp" => %{
      cmd: "sbcl --script",
      builder: :execute
    },

    "Haskell" => %{
      cmd: "runhaskell",
      builder: :execute
    },

    "C" => %{
      cmd: "gcc -std=c99 -lm",
      builder: :build
    },

    "C++" => %{
      cmd: "g++ -std=c++0x",
      builder: :build
    },

    "Lua" => %{
      cmd: "lua",
      builder: :execute
    },

    "Ruby" => %{
      cmd: "ruby",
      builder: :execute
    },

    "Bash" => %{
      cmd: "bash",
      builder: :execute
    },

    "Objective-C" => %{
      cmd: "gcc -Wall -lm -lobjc",
      builder: :build
    },

    "PHP" => %{
      cmd: "php",
      builder: :execute
    },

    "Swift" => %{
      cmd: "swift",
      builder: :execute
    }
  }

  def run({problem, lang, file}) do
    %{cmd: cmd, builder: builder} = @build_machine[lang]
    run(builder, cmd, {problem, lang, file})
  end

  defp run(:build, cmd, {problem, lang, file}) do
    cd = Path.join([".", problem, lang])
    [cmd | flags] = separate_command_from_flags(cmd)

    %{"name" => name} = Regex.named_captures(~r/(?<name>.+)\.(.+)$/, file)
    outfile = name <> ".out"

    System.cmd(cmd, [file, "-o", outfile] ++ flags, cd: cd, stderr_to_stdout: true)
    run(:execute, "bash -c", {problem, lang, outfile})
  end
  defp run(:execute, cmd, {problem, lang, file}) do
    cd = Path.join([".", problem, lang])
    [cmd | flags] = separate_command_from_flags(cmd)

    # Compiled files when error
    if not File.exists?(Path.join(cd, file)) do
      IO.puts "\n#{Path.join(cd, file)} does not exists"
      System.halt(1)
    end

    System.cmd cmd, flags ++ [file], cd: cd, stderr_to_stdout: true
  end

  # Some commands are like "sbcl --script" and I need to split those
  defp separate_command_from_flags(cmd) do
    String.split(cmd, " ")
  end
end

defmodule Consumer do
  use GenServer

  def start_link do
    GenServer.start_link __MODULE__, %{}, name: __MODULE__
  end

  def consume({problem, language, file}, time) do
    GenServer.cast __MODULE__, {problem, language, file, time}
  end

  def output do
    GenServer.cast __MODULE__, :output
  end

  def handle_cast({problem, language, file, time}, state) do
    nested = Map.put(state[problem] || %{}, language, {file, time})
    state = Map.put(state, problem, nested)
    {:noreply, state}
  end
  def handle_cast(:output, state) do
    Renderer.stop()
    IO.puts "Finished all tasks"
    IO.puts ""

    rows =
      state
      |> Map.to_list
      |> Enum.flat_map(fn {problem, languages} ->
        languages
        |> Map.to_list
        |> Enum.map(fn {lang, {solution, time}} ->
          {problem, lang, solution, time}
        end)
      end)
      |> Enum.sort_by(&(elem(&1, 3)), &>=/2)

    slow = Enum.take_while(rows, & elem(&1, 3) >= 60_000_000) # 1 min

    if not Enum.empty?(slow) do
      IO.puts "The following solutions past our time tolerance of one minute:"

      for {problem, lang, solution, time} <- slow do
        time =
          time / 1_000_000
          |> Float.round(2)
          |> Float.to_string

        IO.puts "\t#{problem}/#{lang}/#{solution} (#{time}s)"
      end

      System.halt(1)
    end

    rows =
      rows
      |> Enum.map(fn {problem, lang, solution, time} ->
        time =
          time / 1_000_000
          |> Float.round(2)
          |> Float.to_string

        [problem, lang, solution, (time) <> "s"]
      end)

    rows =
      [["Problem", "Language", "File", "Timing"] | rows]

    col_sizes =
      rows
      |> Enum.reduce([0, 0, 0, 0], fn (row, acc) ->
        row
        |> Enum.map(&String.length/1)
        |> Zipper.zip_with(acc, &max/2)
      end)

    rows
    |> Enum.map(fn row ->
      row
      |> Zipper.zip_with(col_sizes, & String.pad_leading(&1, &2))
      |> Enum.join(" | ")
    end)
    |> Enum.join("\n")
    |> IO.puts

    System.halt(0)

    {:noreply, state}
  end
end

defmodule Zipper do
  def zip_with(as, bs, _f) when length(as) == 0 or length(bs) == 0 do
    []
  end
  def zip_with([a|as], [b|bs], f) do
    [f.(a, b) | zip_with(as, bs, f)]
  end
end

defmodule Renderer do
  @spinner_frames [
    ".  ",
    ".. ",
    "...",
    " ..",
    "  ."
  ]

  use GenServer

  def start_link do
    pool_size = Settings.get(:pool_size)
    labels = for _ <- 1..pool_size, do: nil
    GenServer.start_link __MODULE__, labels, name: __MODULE__
  end

  def init(labels) do
    {rendered, labels} = render_labels(labels)
    IO.write rendered
    {:ok, labels}
  end

  def render do
    :ok = GenServer.cast __MODULE__, :render
  end

  def set_label(id, label) do
    :ok = GenServer.cast __MODULE__, {:set_label, id, label}
  end

  def delete_label(id) do
    :ok = GenServer.cast __MODULE__, {:delete_label, id}
  end

  def stop do
    :ok = GenServer.cast __MODULE__, :stop
  end

  def handle_info(:timeout, state) do
    render()
    {:noreply, state}
  end

  def handle_cast(:render, labels) do
    IO.write Spinner.erase_lines(Enum.count(labels) - 1)
    {rendered, labels} = render_labels(labels)
    IO.write rendered
    {:noreply, labels, 100}
  end
  def handle_cast({:set_label, id, label}, labels) do
    render()
    {:noreply, List.update_at(labels, id - 1, fn _ -> {@spinner_frames, label} end)}
  end
  def handle_cast({:delete_label, id}, labels) do
    render()
    {:noreply, List.update_at(labels, id - 1, fn _ -> nil end)}
  end
  def handle_cast(:stop, labels) do
    IO.write Spinner.erase_lines(Enum.count(labels) - 1)
    {:stop, "Done", labels}
  end

  defp render_labels(labels) do
    {lines, labels} =
      labels
      |> Enum.map_reduce([], fn
        (nil, acc) ->
          {"Waiting", acc ++ [nil]}

        ({[], label}, acc) ->
          frame = hd @spinner_frames
          text = "#{frame} #{label}"
          {text, acc ++ [{tl(@spinner_frames), label}]}


        ({[frame | frames], label}, acc) ->
          text = "#{frame} #{label}"
          {text, acc ++ [{frames, label}]}
      end)

    {Enum.join(lines, "\n"), labels}
  end
end

defmodule Spinner do
  @esc "\u001B["
  @erase_line @esc <> "2K"
  @cursor_left @esc <> "G"

  def cursor_up, do: cursor_up(1)
  def cursor_up(count) do
    @esc <> Integer.to_string(count) <> "A"
  end

  def erase_lines(count) do
    ups =
      0..count
      |> Enum.map(fn _ -> @erase_line end)
      |> Enum.intersperse(cursor_up())
      |> Enum.join("")

    ups <> @cursor_left
  end
end


Settings.start_link()
CLI.run()
