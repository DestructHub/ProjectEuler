#Author: tkovs

def solve
    sum_square = (1..100).map{|x| x * x}.inject(:+)
    square_sum = (1..100).inject(:+) * (1..100).inject(:+)

    return(square_sum - sum_square)
end

puts(solve)