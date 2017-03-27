class Integer
  def is_pentagonal? # Inverse of pentagonal function
    ((Math.sqrt((24 * self) + 1) + 1) % 6) == 0
  end

  def generate_hexagonal
    self * ((self * 2) - 1)
  end
end

class TrianglePentagonHexagon
  attr_accessor :final
  def initialize
    @final = 0
  end

  def find_pentagonal # All hexagonal are triagonal
    counter = 144
    until final > 0
      hex = counter.generate_hexagonal
      @final = hex if hex.is_pentagonal?
      counter += 1
    end
  end
end

euler = TrianglePentagonHexagon.new
euler.find_pentagonal
p euler.final