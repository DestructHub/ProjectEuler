def palindrome(n)
    return (n.to_s().eql?(n.to_s().reverse()))
end

def solve
    list = (1..999).flat_map{|x| (1..999).map {|y| x * y}}
    return list.select{|x| palindrome(x).eql?(true)}.max()
end

puts(solve)