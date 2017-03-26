{-- Author: Manoel Vilela --}

fat :: (Num b, Enum b) => b -> b
fat n = product [1..n]

choose :: (RealFrac a, Enum a, Integral b) => a -> a -> b
choose n k = floor $ fat n /(fat k * fat (n - k))

bigCombs :: (RealFrac t, Enum t) => t -> Int
bigCombs n = length [x | k <- [1..n], let x = choose n k, x > 1000000]

solution :: Int
solution = sum [k | n <- [1..100], let k = bigCombs n]

main :: IO()
main = print solution
