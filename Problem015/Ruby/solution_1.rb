#Author: tkovs
#Translation of the Haskell code P016

def solve
    return ((1..40).inject(:*) / ((1..20).inject(:*) ** 2))
end

puts(solve)