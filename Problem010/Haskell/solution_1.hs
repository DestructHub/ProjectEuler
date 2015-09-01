-- Author: G4BB3R
-- Performance: 7643.2s (How to improve ?)

primes :: [Int]
primes = sieve [2..]
  where sieve :: [Int] -> [Int] ;
  		sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0] ;
  		sieve [] = []

main :: IO ()
main = print $ sum $ takeWhile (< 2000000) primes
