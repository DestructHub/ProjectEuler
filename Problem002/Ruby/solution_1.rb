def fib(n)
    a = 0
    b = 1
    sequence = [a] # initialize

    while (b < n)
        sequence.push(b)

        temp, a = a, b
        b = a + temp
    end

    return(sequence)
end

def solve
    fib(4000000).select{|n| n.even?}.inject(:+)
end

puts solve