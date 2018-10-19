:math.pow(2, 1000) |> round
                   |> to_charlist
                   |> Enum.map(fn (c) -> c - hd('0') end)
                   |> Enum.sum
                   |> inspect
                   |> IO.puts
