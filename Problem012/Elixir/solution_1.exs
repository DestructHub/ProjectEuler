# Author: lubien

defmodule Euler12 do
  def solve do
    Stream.iterate(1, &(&1 + 1))
      |> Stream.scan(&(&1 + &2))
      |> Stream.drop_while(fn i -> count_divisors(i) < 500 end)
      |> Enum.take(1)
      |> hd
  end

  def count_divisors(n) do
    sqrt = :math.sqrt(n)

    count = 1..(round(sqrt))
      |> Stream.filter(fn i -> rem(n, i) == 0 end)
      |> Enum.count

    if sqrt * sqrt == n do
      count * 2
    else
      count * 2 - 1
    end
  end
end

Euler12.solve
  |> IO.puts

