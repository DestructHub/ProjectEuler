:math.pow(2, 1000) |> round
                   |> to_char_list
                   |> Enum.map(fn (c) -> c - hd('0') end)
                   |> Enum.sum
                   |> inspect
                   |> IO.puts