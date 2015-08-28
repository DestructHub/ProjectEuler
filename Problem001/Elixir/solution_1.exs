# Author: G4BB3R

1..999 |> Enum.to_list
       |> Enum.filter(&(rem(&1, 3) == 0 or rem(&1, 5) == 0))
       |> Enum.sum
       |> IO.puts
	