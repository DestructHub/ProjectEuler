-- Author: tkovs

numbers :: [Integer]
numbers = [a^b | a <- [1..100], b <- [1..100]]

sumDigits :: Integer -> Int
sumDigits x = sum $ map (\x -> (fromEnum x) - 48) $ show x

solve :: Int
solve = maximum $ map sumDigits numbers

main :: IO ()
main = do
    print solve