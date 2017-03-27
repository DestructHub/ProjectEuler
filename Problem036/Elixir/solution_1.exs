defmodule DoubleBase do
  def palindrome(lim) do
    (1..lim)
      |> Stream.map(fn a -> Integer.to_string(a) end)
      |> Stream.filter(fn b -> pal?(b) end)
      |> Stream.map(fn c -> Integer.to_string(String.to_integer(c),2) end)
      |> Stream.filter(fn d -> pal?(d) end)
      |> Stream.map(fn e -> String.to_integer(e,2) end)
      |> Enum.reduce(fn f,g -> f + g end)
      |> IO.inspect
  end

  def pal?(n) do
    n == String.split(n,"",trim: true)
      |> Enum.reverse()
      |> Enum.join()
  end
end

DoubleBase.palindrome(1_000_000)