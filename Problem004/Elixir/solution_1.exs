isPalindrome = fn num -> num
	|> Integer.to_string
	|> String.reverse
	|> String.to_integer
	|> (fn x -> x == num end).()
end

	for x <- 1..999,
	    y <- 1..999,
	    isPalindrome.(x * y) do
	    	x * y
	end
	|> Enum.max
	|> IO.puts
	