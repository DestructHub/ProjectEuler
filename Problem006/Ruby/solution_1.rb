#Author: tkovs

def solve
    list = (1..100)

    sum_square = list.map{|x| x * x}.inject(:+)
    square_sum = list.inject(:+) * list.inject(:+)

    return(square_sum - sum_square)
end

puts(solve)