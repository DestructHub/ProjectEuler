# Author: lubien

(
  for a <- 2..100,
      b <- 2..100,
  do: :math.pow(a, b) |> round
)
  |> Stream.uniq
  |> Enum.count
  |> IO.puts
