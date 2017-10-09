d :: Int -> Int
d n = sum [x | x <- [1..div n 2], mod n x == 0]

amicable :: Int -> Bool
amicable n = (d n /= n && n == d (d n))

main :: IO ()
main = do
    print . sum $ filter amicable [1..10000]
