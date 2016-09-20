def sum_digits(value)
  value.to_s
       .chars
       .map{|x| x.to_i ** 5}
       .reduce(:+)
end

puts (2..200000).to_a
                .select{|x| sum_digits(x) == x}
                .reduce(:+)
