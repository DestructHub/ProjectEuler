# Author: lubien

defmodule Euler14 do
  def solve() do
    largest_collatz(1, {0, 0})
  end

  defp largest_collatz(1_000_000, {_size, current}), do: current
  defp largest_collatz(n, {size, _current} = acc) do
    current_size = collatz(n)

    if current_size > size do
      largest_collatz n + 1, {current_size, n}
    else
      largest_collatz n + 1, acc
    end
  end

  def collatz(n), do: collatz(n, 1)

  defp collatz(1, acc), do: acc
  defp collatz(n, acc) do
    next = if rem(n, 2) == 0 do
      div(n, 2)
    else
      (3 * n) + 1
    end

    collatz(next, acc + 1)
  end
end

Euler14.solve
  |> IO.puts

