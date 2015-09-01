# Author: G4BB3R

defmodule Problem007 do

	def isPrime(1), do: false
	def isPrime(2), do: true
	def isPrime(3), do: true
	def isPrime(n), do: (2..(n - 1)) |> Enum.find(fn x -> rem(n, x) == 0 end) |> (fn found -> found == nil end).()

	def prime10001           , do: prime10001(1, 0)
	defp prime10001(x, 10001), do: x + 1
	defp prime10001(x, prime), do: prime10001(x + 1, prime + (if isPrime x do 1 else 0 end))

end

#Enum.map 1..100, &(IO.puts (Integer.to_string(&1) <> ": " <>  (if Problem007.isPrime &1 do "SIM" else "NAO" end)))

IO.puts Problem007.prime10001
