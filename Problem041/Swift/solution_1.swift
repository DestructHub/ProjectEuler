import Glibc

func swap (str:[Character], i:Int, j:Int) -> [Character]
{
  var newStr = str
  let c = str[i]
  newStr.removeAtIndex(i)
  newStr.insert(str[j], atIndex:i)
  newStr.removeAtIndex(j)
  newStr.insert(c, atIndex:j)
  return newStr
}

func isPandigitalPrimeTest(n:Double) -> Bool
{
  if n % 2 == 0
  {
    return false
  }
  else
  {
    let end = sqrt(n)
    var i = Double(3)
    while i <= end
    {
      if (n % i == 0)
      {
        return false
      }
      i += 2
    }
  }

  return true
} 

func newStringScope(n:Int) -> String 
{
  var i = n - 1
  var scope = ""

  while i > 0
  {
    scope += String(i)
    i -= 1
  }

  return scope 
}

var maxPandigitalPrime = -1

func permuteString(str:[Character], i:Int, length:Int) 
{
  if length == i
  {
    if (isPandigitalPrimeTest(Double(String(str))!))
    {
      maxPandigitalPrime = max (maxPandigitalPrime, Int(String(str))!)
    }

    return
  }

  var newStr = str;

  for j in i..<length
  {
    newStr = swap(newStr, i:i, j:j)
    permuteString(newStr, i:i+1, length:length)
    newStr = swap(newStr, i:i, j:j) 
  }

  return
}

var idx = 9 
while idx > 0
{
  var fixedScope = Array((String(idx) + newStringScope(idx)).characters)
  
  permuteString(fixedScope, i:1, length:fixedScope.count)

  idx -= 1
} 

print (maxPandigitalPrime) 
