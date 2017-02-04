defmodule Prime do
  def solve(num), do: solve(num, 2)
  defp solve(num, acc) when num <= acc, do: num |> IO.puts()
  defp solve(num, acc) when num > acc and rem(num, acc) == 0 do
    num |> div(acc) |> solve(acc + 1)
  end
  defp solve(num, acc) when num > acc and rem(num, acc) != 0 do
    num |> solve(acc + 1)
  end
end

600851475143 |> Prime.solve()
