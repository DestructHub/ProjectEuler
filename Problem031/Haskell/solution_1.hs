getTupleValue :: (Int, Int, Int, Int, Int, Int, Int, Int) -> Int
getTupleValue (p1, p2, p5, p10, p20, p50, l1, l2) =
    p1        +
    p2  *  2  +
    p5  *  5  +
    p10 * 10  +
    p20 * 20  +
    p50 * 50  +
    l1  * 100 +
    l2  * 200

coinsPermutations :: [(Int, Int, Int, Int, Int, Int, Int, Int)]
coinsPermutations = [(p1, p2, p5, p10, p20, p50, l1, l2) | p1  <- [1..200 `div` 1]
                                                         , p2  <- [1..200 `div` 2]
                                                         , p5  <- [1..200 `div` 5]
                                                         , p10 <- [1..200 `div` 10]
                                                         , p20 <- [1..200 `div` 20]
                                                         , p50 <- [1..200 `div` 50]
                                                         , l1  <- [1..200 `div` 100]
                                                         , l2  <- [1..200 `div` 200]
                                                         ]

permutationsWith200p :: Int
permutationsWith200p = foldr (\tuple acc -> acc + if getTupleValue tuple == 200 then 1 else 0) 0 coinsPermutations

main :: IO ()
main = print permutationsWith200p
