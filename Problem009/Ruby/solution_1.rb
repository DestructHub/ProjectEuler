#Author: tkovs

def test(a, b, c)
    return false unless (a*a + b*b == c*c)
    return false unless (a + b + c == 1000)

    return true
end

def solve
    x = (1..444)
    x.each{|a| x.each{|b| x.each{|c| return (a * b * c) if (test(a, b, c))}}}
end

puts solve