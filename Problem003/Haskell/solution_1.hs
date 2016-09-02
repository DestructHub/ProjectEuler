prime_acc :: Integer -> Integer -> Integer
prime_acc value acc
    | acc < value = if mod value acc == 0 then 
                        prime_acc (div value acc) (acc + 1)
                    else
                        prime_acc value (acc + 1)
    | otherwise = acc

prime :: Integer -> Integer
prime x = prime_acc x 2

main :: IO ()
main = print $ prime 600851475143
