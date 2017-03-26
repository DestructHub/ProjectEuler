{-- Author: Manoel Vilela --}

import Data.Char (chr, ord)
import Data.Bits (xor)

parseFile :: String -> [Int]
parseFile s = read ("[" ++ s ++ "]")

passwords :: [[Int]]
passwords = [map ord [a,b,c] | a <- ['a'..'z'],
                               b <- ['a'..'z'],
                               c <- ['a'..'z']]

applyKey :: [Int] -> [Int] -> [Int]
applyKey content pass = [ x `xor` y | (x,y) <- pairs]
  where pairs = zip content $ concat $ repeat pass


checkIt :: [Int] -> Bool
checkIt = all commonAscii
  where commonAscii x = x `elem` asciiNumbers ++ asciiPunct
                        || asciiLower x || asciiUpper x
        asciiNumbers = [48..57]
        asciiPunct = [32,33,34,39,40,41,44,45,46,58,59]
        asciiLower x = x >= 97 && x <= 122
        asciiUpper x = x >= 65 && x <= 90

decrypt :: [Int] -> [Int]
decrypt codes = head [decrypted | pass <- passwords,
                             let decrypted = applyKey codes pass,
                             checkIt decrypted]

main = do content <- readFile "p059_cipher.txt"
          print $ sum $ decrypt $ parseFile (head (lines content))
