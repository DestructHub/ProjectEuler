def fat(n)
    return 1 if n == 0

    (1..n).to_a
          .reduce(:*)
          .to_i
end

def check(n)
    m = n.to_s
         .chars
         .map{|x| fat(x.to_i)}
         .reduce(:+)

    n == m
end

puts (3..50000).to_a.select{|x| check(x)}.reduce(:+)
