box = fn b -> (4 * (round(:math.pow(((2 * b) + 1), 2))) - (12 * b)) end

Enum.map(1..500, fn x -> box.(x) end)
  |> Enum.reduce(fn c,d -> c + d end)
  |> Kernel.+(1)
  |> IO.puts