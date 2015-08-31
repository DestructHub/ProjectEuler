-- Author: G4BB3R

import Data.List (find)
import Data.Maybe (fromJust)

smallest :: Int
smallest = fromJust $ find (\x -> all (\y -> rem x y == 0) [11..20]) [1..]

main = print smallest