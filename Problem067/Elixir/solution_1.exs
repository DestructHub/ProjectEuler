defmodule MaximumPath do
  def find([left|_]) when length(left) == 1 do
    left
  end

  def find([left|[mid|right]]) when length(left) > 0 do
    mid = for n <- (0..(length(left)-2)), do: Integer.to_string(new_val(left,mid,n))
    find([mid|right])
  end

  def new_val(a,b,c), do: String.to_integer(Enum.at(b,c)) + Enum.max([String.to_integer(Enum.at(a,c)),String.to_integer(Enum.at(a,c+1))])
end

defmodule Triangle do
  def input(file) do
    case File.read(file) do
      {:ok, body}     ->
        body
          |> String.split("\n", trim: true)
          |> Enum.reverse()
          |> Enum.map(fn x -> String.split(x," ", trim: true) end)
          |> MaximumPath.find()
          |> IO.puts
      {:error,reason} ->
        :file.format_error(reason)
    end
  end
end

Triangle.input("../Python/p067_triangle.txt")