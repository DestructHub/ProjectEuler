-- Author: G4BB3R

import Data.List (sort, nub)

main :: IO ()
main = print $ sum $ nub [ xy | x <- [1..9999 :: Int]
                              , y <- [1..99   :: Int]
                              , let xy = x * y
                              , (== "123456789") . sort $ show x ++ show y ++ show xy
                              ]