# Author: lubien

defmodule Euler5 do
  def solve(n) do
    1..n |> Enum.reduce(&lcm/2)
  end

  def lcm(x, y), do: div(x * y, gcd(x, y))

  def gcd(x, 0), do: x
  def gcd(x, y) do
    gcd(y, rem(x, y))
  end
end

Euler5.solve(20)
  |> IO.puts

