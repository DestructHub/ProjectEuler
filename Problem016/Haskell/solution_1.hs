import Data.Char (digitToInt)

sumDigits :: Integer -> Int
sumDigits = sum . map digitToInt . show

main :: IO ()
main = print . sumDigits $ (2 ^ (1000 :: Integer))
