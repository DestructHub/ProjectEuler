-- Author: G4BB3R

import Data.List (find)
import Data.Maybe (isNothing)

isPrime :: Int -> Bool
isPrime x
	| x == 1    = False
	| x <= 3    = True
	| otherwise = isNothing $ find ((== 0) . rem x) [2..x - 1]

prime10001 :: Int
prime10001 = prime' 2 0 where
	prime' x prime = if prime == 1001 then x + 1 else prime' (x + 1) (prime + (if isPrime x then 1 else 0))

main :: IO ()
main = print prime10001

