class PermutationMultiples
  attr_accessor :prime_array,:lowest
  attr_reader   :finish
  def initialize(finish)
    @finish = finish
  end

  def find_permutations # Chose arbitrary number range => only checks until is true
    (1).upto(finish) { |num| return @lowest = num if six_time_permutation?(num) }
  end

  def six_time_permutation?(num) # Only check if each proceeding multiple is a permutation
    sorted = num.to_s.split("").sort
    (2..6).each { |n| return nil unless sorted == (n*num).to_s.split("").sort }
  end
end

euler = PermutationMultiples.new(1000000)
euler.find_permutations
p euler.lowest