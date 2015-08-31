# Author: G4BB3R

1..999999999999 |> Enum.find(fn x -> Enum.all? 11..20, &(rem(x, &1) == 0) end)
                |> IO.puts