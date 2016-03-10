# Author: tkovs

def solve
	(0..999).select{|n| n % 3 == 0 || n % 5 == 0}.inject(:+)
end

puts(solve)