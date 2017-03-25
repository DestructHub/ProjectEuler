-- Author: Manoel Vilela
-- Time: ~ 51s (how to improve?)
import Data.Ratio (numerator, denominator)

-- recursive part
continuedFraction :: Rational -> Rational -> Rational
continuedFraction _ 0 = 0
continuedFraction a 1 = a
continuedFraction a n = a + 1/continuedFraction a (n-1)

sqrt2Recursive :: Integer -> Rational
sqrt2Recursive 0 = 0
sqrt2Recursive n = 1 + 1/continuedFraction 2 (toRational n)

numGreaterThanDen :: Rational -> Bool
numGreaterThanDen r = let n = length $ show $ numerator r
                          d = length $ show $ denominator r
                       in n > d

main :: IO()
main = print $ length $ filter numGreaterThanDen $ map sqrt2Recursive [1..1000]
