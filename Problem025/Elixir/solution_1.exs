# Author: lubien

Stream.unfold(
  {1, 1}, fn {a, b} ->
    next = a + b;
    case length(Integer.digits(a)) do
      1_000 -> nil
      _ -> {next, {next, a}}
    end
  end
)
  |> Stream.with_index
  |> Enum.to_list
  |> List.last
  |> elem(1)
  |> (fn x -> x + 3 end).()
  |> IO.inspect
