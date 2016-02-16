import Glibc

func is9Pandigital(value:String) -> Bool
{
  return String(value.characters.sort()) == "123456789"
}

func nDigitsInMult(n1:Int, n2:Int) -> Int
{
  return Int(floor((log10(Double(n1) + log10(Double(n2))) + 1)))
}

var max9Pandigital = -1
var i = 1
let maxNumber = Int(pow(10, 9 / 2))

while i < maxNumber 
{
  var concat = ""
  for j in 1...9
  {
    if concat.characters.count + nDigitsInMult(i, n2:j) > 9
    {
      break
    }
    
    concat += String(i * j)
    if (is9Pandigital(concat))
    {
      max9Pandigital = max(max9Pandigital, Int(concat)!)
    }
  }

  i+=1
}

print (max9Pandigital)
