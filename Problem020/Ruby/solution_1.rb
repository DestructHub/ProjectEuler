#Author: tkovs

def solve
    1.upto(100).inject(:*).to_s.split('').map{|x| x.to_i}.inject(:+)
end

puts(solve)