import Data.Function (fix)

prime f value acc
    | acc >= value = acc
    | mod value acc == 0 = f (div value acc) (acc + 1)
    | otherwise = f value (acc + 1)

main :: IO ()
main = print $ fix prime 600851475143 2
