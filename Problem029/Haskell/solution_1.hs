import Data.List

list :: [Integer] -- Not Int
list = [a ^ b | a <- [2..100], b <- [2..100]]

main :: IO ()
main = print . length $ f list
         where f = map head . group . sort
