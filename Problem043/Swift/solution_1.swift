// send the items from the right to the left 
func permute(array:[Int]) -> [Int]
{
  var mutArr = array
  var i = mutArr.count - 2
  loop: while true
  {
    switch i
    {
      case let x where x < 0: return [] 
      case let x where mutArr[x] < mutArr[x+1]: break loop
      default: i -= 1
    }
  }

  var j = 1
  while j + i < mutArr.count - j
  {
    let n = mutArr[j + i]
    mutArr[j + i] = mutArr[mutArr.count - j]
    mutArr[mutArr.count - j] = n
    j += 1
  }

  j = i + 1
  while mutArr[j] <= mutArr[i]
  {
    j += 1
  }

  let n = mutArr[i]
  mutArr[i] = mutArr[j]
  mutArr[j] = n

  return mutArr
}

let primes = [2, 3, 5, 7, 11, 13, 17]
let numbers = Array("0123456789".characters).map{Int(String($0))!}
var arr = permute(numbers)
var sum:UInt64 = 0
var count = 0

while !arr.isEmpty  
{
  var i = 0

  while i < primes.count
  {
    let n1 = Int(arr[i + 1]) * 100
    let n2 = Int(arr[i + 2]) * 10
    let n3 = Int(arr[i + 3])

    if (n1+n2+n3) % primes[i] != 0
    {
      break 
    }

    i += 1
  }

  if (i == primes.count)
  {
    var str = arr.map { String($0) }.joinWithSeparator("")
    sum += UInt64(str)!
    count += 1
  }

  arr = permute(arr)
}

print(sum)
