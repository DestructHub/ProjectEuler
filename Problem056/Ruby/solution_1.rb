#Author: tkovs

def solve
    #generate list a^b | a <- [1..99] and b <- [1..99]
    numbers = (1..99).flat_map{|a| (1..99).map{|b| a ** b}}
    #map digits' sum of each number
    sumDigits = numbers.map{|element| element.to_s.split('').map{|digit| digit.to_i}.inject(:+)}
    #return the maximum value
    return(sumDigits.max)
end

puts(solve)