-- Author: G4BB3R
-- Performance: 38.8s (Improved: 196x faster)

primes = 2 : ([3..] `minus` composites)
    where composites = union [multiples p | p <- primes]

multiples n = map (n*) [n..]

(x:xs) `minus` (y:ys) | x < y  = x :   (xs `minus` (y : ys))
                      | x == y = xs        `minus` ys
                      | x > y  = (x : xs)  `minus` ys

union = foldr merge []
  where
    merge  (x : xs) ys = x : merge' xs ys
    merge' (x : xs) (y : ys) | x < y  = x : merge' xs (y : ys)
                             | x == y = x : merge' xs ys
                             | x > y  = y : merge' (x : xs) ys

main :: IO ()
main = print $ sum $ takeWhile (< 2000000) primes
