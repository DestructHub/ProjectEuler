import Foundation

var lastTriangleValue:Double = 285
var res:Double = 0

typealias Polynomial = (a:Double, c:Double)

let P:Polynomial = (a:3, c:2)
let H:Polynomial = (a:2, c:1)
let PH_bModule:Double = 1

while true
{
  lastTriangleValue += 1 
  res = (pow(lastTriangleValue, 2) + lastTriangleValue) / 2
  let Pn = (PH_bModule + sqrt(PH_bModule + 4 * P.a * (P.c * res))) / (2 * P.a)
  let Hn = (PH_bModule + sqrt(PH_bModule + 4 * H.a * (H.c * res))) / (2 * H.a)

  if floor(Pn) == Pn && floor(Hn) == Hn
  { 
    break
  }
}

#if os(OSX) || os(iOS) || os(watchOS) || os(tvOS) 
  print(String(format: "%.0f", res))
#else
  print(NSString(format: "%.0f", res))
#endif

