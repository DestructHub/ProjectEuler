def test(a,b,c)
    return(false) unless (a*a + b*b == c*c)
    return(false) unless (a + b + c == 1000)

    return true
end

def solve
    (1..444).each{|a| (1..444).each{|b| (1..444).each{|c| return (a*b*c) if (test(a,b,c))}}}
end

puts(solve)