# Author: lubien

for a <- 1..444,
    b <- 1..444,
    c <- [1000 - b - a],
    a * a + b * b == c * c
  do a * b * c end
  |> List.first
  |> IO.puts
