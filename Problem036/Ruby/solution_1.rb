def binary(value)
    value.to_s(2)
end

def palindrome(value)
    value.to_s.eql?(value.to_s.reverse)
end

def double_base(value)
    palindrome(value) && palindrome(binary(value))
end

puts (0..999999)
        .to_a
        .select{|x| double_base(x)}
        .reduce(:+)
