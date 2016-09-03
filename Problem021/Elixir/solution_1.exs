# Author: lubien

defmodule Euler21 do
  def solve do
    1..10_000
      |> Stream.filter(&amicable/1)
      |> Enum.reduce(&sum/2)
  end

  def d(1), do: 1
  def d(n) do
    1..(div(n, 2))
      |> Stream.filter(&(rem(n, &1) == 0))
      |> Enum.reduce(&sum/2)
  end

  def amicable(a) do
    amic = d(a)

    amic != a && d(amic) == a
  end

  defp sum(x, y), do: x + y
end

Euler21.solve
  |> IO.puts

