var nextNumber = 1  
var primeArr:[Int] = [2,3,5,7]
var checkArr:[Int] = [] 

loop:while true
{
  nextNumber += 1
  var remainder = nextNumber 
  var count = 0
 
  for i in 0..<primeArr.count
  {
    if remainder % primeArr[i] == 0
    { 
      while remainder % primeArr[i] == 0 { remainder /= primeArr[i] }
      count += 1
      if remainder == 1 && count == 4 
      {
        if checkArr.count < 3  { checkArr.append(nextNumber) }
        else if nextNumber - 1 == checkArr[2] && nextNumber - 2 == checkArr[1] && nextNumber - 3 == checkArr[0] 
        {
          print(checkArr[0])
          break loop
        }
        else
        {
          checkArr.removeAtIndex(0)
          checkArr.append(nextNumber)
        }
      }
      else if remainder == 1
      {
        break
      } 
    } 
  }

  if remainder == nextNumber { primeArr.append(remainder); }
}
