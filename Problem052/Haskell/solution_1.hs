{-- Author: Manoel Vilela
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that
2x, 3x, 4x, 5x, and 6x, contain the same digits.
--}


import Data.List (sort, nub)

sameDigits :: Integer -> Integer -> Bool
sameDigits x y = f x == f y
  where f k = sort $ nub $ show k

check :: Integer -> Bool
check x = all (sameDigits x) $  map (* x) [2..6]

solution :: Integer
solution = head [x | x <- [1..], check x]

main :: IO()
main = print solution
