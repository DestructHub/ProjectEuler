import Data.List (permutations, sort)
import Data.Char (intToDigit)

main :: IO ()
main = do
    putStr $ map intToDigit list
      where list = (sort . permutations $ [0..9]) !! 999999
