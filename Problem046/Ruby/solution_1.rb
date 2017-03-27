class Goldbach
  attr_accessor :prime_array,:square_array,:sums
  attr_reader   :finish,:all_composites,:squared_double,:composite
  def initialize(finish)
    @finish      = finish
    @composite   = 0
    @prime_array = (3..finish).step(2).to_a.insert(0,2)
  end

  def find_goldbach
    @composite = all_composites.find { |n| !sums.include?(n) }
  end

  def sieve_of_eratosthenes
    (4..prime_array.last).each { |i| prime_array.delete_if { |num| num % i == 0 && num > i } }
  end
  
  def generate_composites
    @all_composites = (2..finish).select { |n| n.odd? && !prime_array.include?(n) }
  end

  def generate_squares
    @squared_double = (0..(finish/100)).map { |n| 2*(n**2) }
  end

  def sum_primes_and_squares
    @sums = prime_array.flat_map { |i| squared_double.map { |j| i + j } }
  end
end

euler = Goldbach.new(10000)
euler.sieve_of_eratosthenes
euler.generate_composites
euler.generate_squares
euler.sum_primes_and_squares
euler.find_goldbach
p euler.composite