Stream.unfold({0, 1}, fn {a, b} -> {a, {b, a + b}} end)
|> Stream.filter(&(rem(&1, 2) == 0))
|> Enum.reduce_while(0, fn (i, acc) -> if (i < 4_000_000), do: {:cont, acc + i}, else: {:halt, acc} end)
