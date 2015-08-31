-- Author: G4BB3R

isPalindrome :: Int -> Bool
isPalindrome x = show x == (reverse . show $ x)

largestPalindrome :: Int
largestPalindrome = maximum [x * y | x <- [1..999], y <- [1..999], isPalindrome $ x * y]

main :: IO ()
main = print largestPalindrome
