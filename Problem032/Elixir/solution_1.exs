# Author: G4BB3R

	for x <- 1..9999,
		y <- 1..99,
		xy = x * y,
		'123456789' == Enum.sort(to_charlist(Integer.to_string(x) <> Integer.to_string(y) <> Integer.to_string(xy)))
	do xy end

	|> Enum.uniq
	|> Enum.sum
	|> IO.puts
