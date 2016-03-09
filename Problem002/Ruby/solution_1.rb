# Author: tkovs

def fib(n)
    a, b = 0, 1
    sequence = [a] # initialize

    while (b < n)
        sequence.push(b)
        a, b = b, a + b
    end

    return(sequence)
end

def solve
    fib(4000000).select{|n| n.even?}.inject(:+)
end

puts(solve)