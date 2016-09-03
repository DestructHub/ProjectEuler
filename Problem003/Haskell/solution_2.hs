prime value acc
    | acc >= value = acc
    | mod value acc == 0 = prime (div value acc) (acc + 1)
    | otherwise = prime value (acc + 1)

main :: IO ()
main = print $ prime 600851475143 2
