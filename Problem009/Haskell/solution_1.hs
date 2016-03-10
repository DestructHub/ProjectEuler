-- Author: G4BB3R
-- Help: tkovs

triangulo = head [(a, b, c) | a <- [1..444], b <- [a..444], c <- [1000 - b - a], a ^ 2 + b ^ 2 == c ^ 2]

main = print $ let (a, b, c) = triangulo in a * b * c