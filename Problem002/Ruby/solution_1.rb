def fib(n)
    a = 0
    b = 1
    sequence = [a] # initialize [a, b]

    while (b < n)
        sequence.push(b)

        temp = a
        a = b
        b = temp + a
    end

    return(sequence)
end

def solve
    fib(4000000).select{|n| n.even?}.inject(:+)
end

puts solve