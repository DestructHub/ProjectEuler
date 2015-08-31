# Author: G4BB3R

x = 1..100 |> Enum.sum
           |> :math.pow(2)
	
y = 1..100 |> Enum.to_list
		   |> Enum.map(&:math.pow(&1, 2))
		   |> Enum.sum

IO.puts round(x - y)
