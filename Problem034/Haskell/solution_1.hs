import Data.Char (digitToInt)

fat :: Int -> Int
fat n = product [1..n]

check :: Int -> Bool
check n = (n == m)
  where m = sum . map fat $ map digitToInt $ show n

main :: IO ()
main = do
    print . sum $ filter check [3..50000]
