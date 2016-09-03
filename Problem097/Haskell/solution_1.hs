main :: IO ()
main = putStrLn . reverse . take 10 . reverse $ x
    where x = show (28433 * 2^7830457 + 1)
