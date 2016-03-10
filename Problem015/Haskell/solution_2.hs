-- Author: G4BB3R

main :: IO ()
main = print $ div (fat 40 :: Integer) (fat 20 ^ (2 :: Integer))
         where fat = product . enumFromTo 1