#Author: tkovs

def solve
    return (1..1000).map{|x| x ** x}.inject(:+).modulo(10 ** 10)
end

puts (solve)