{-
The series, 1¹ + 2¹ + 3³ + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000^1000.
-}

main :: IO ()
main = putStrLn . reverse . take 10 . reverse . show . sum $ map (\x -> x^x) [1..1000]