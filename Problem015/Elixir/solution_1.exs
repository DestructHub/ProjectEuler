# Author: G4BB3R

defmodule Fat do

	def fatorial(1), do: 1
	def fatorial(n), do: n * fatorial(n - 1)

end

	IO.puts round(Fat.fatorial(40) / round(:math.pow(Fat.fatorial(20), 2)))
