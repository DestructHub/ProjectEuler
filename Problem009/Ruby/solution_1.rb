#Author: tkovs

def solve
    x = (1..444)
    x.each{|a| x.each{|b| [1000 - b - a].each{|c| return (a * b * c) if (a*a + b*b == c*c)}}}
end

puts(solve)