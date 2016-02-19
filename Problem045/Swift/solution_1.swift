import Foundation

extension Double 
{
    func formatNoDecimal() -> String 
    {
        return String(format: "%.0f", self)
    }
}

var lastTriangleValue:Double = 285
var res:Double = 0

typealias Polynomial = (a:Double, b:Double, c:Double)

let P:Polynomial = (a:3, b:-1, c:2)
let H:Polynomial = (a:2, b:-1, c:1)

while true
{
  lastTriangleValue += 1 
  res = (pow(lastTriangleValue, 2) + lastTriangleValue) / 2
  let Pn = (-P.b + sqrt(pow(P.b, 2) + 4 * P.a * (P.c * res))) / (2 * P.a)
  let Hn = (-H.b + sqrt(pow(H.b, 2) + 4 * H.a * (H.c * res))) / (2 * H.a)

  if floor(Pn) == Pn && floor(Hn) == Hn
  { 
    break
  }
}

print(res.formatNoDecimal())
