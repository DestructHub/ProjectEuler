-- Author: G4BB3R
-- Performance is really bad and with brute force style.
-- I need to find a better solution

triangulo = head [(a, b, c) | a <- [1..444], b <- [a..444], c <- [b..444], a ^ 2 + b ^ 2 == c ^ 2, a + b + c == 1000]

main = print $ let (a, b, c) = triangulo in a * b * c