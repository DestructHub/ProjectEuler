-- Author: G4BB3R

getCollatzSequenceLen :: Int -> Int
getCollatzSequenceLen 1 = 1
getCollatzSequenceLen x = 1 + getCollatzSequenceLen (if even x then x `div` 2 else 3 * x + 1)

getHighestCollatz :: (Int, Int)
getHighestCollatz = getHighestCollatz' 1 (0, 0) where
    getHighestCollatz' :: Int -> (Int, Int) -> (Int, Int)
    getHighestCollatz' 999999 len = len
    getHighestCollatz' n (index, len) = let len' = getCollatzSequenceLen n in
        if len' > len then
            getHighestCollatz' (n + 1) (n, len')
        else
            getHighestCollatz' (n + 1) (index, len)


main :: IO ()
main = print getHighestCollatz

