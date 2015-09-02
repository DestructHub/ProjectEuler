triangleList :: [Int]
--triangleList = map ((\xs -> (sum xs, xs)) . enumFromTo 1) [1..]
triangleList = map (\n -> n * (n + 1) `div` 2) [1..]

main :: IO ()
main = print $ triangleList !! 501

-- Nao ta dando certo, que houve ? :(