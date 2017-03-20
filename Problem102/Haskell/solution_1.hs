-- Autor: Manoel Vilela

-- Generate the inequalities as delimiters based on the functions whose coincides with
-- the segments of the triangle. If a arbitrary point (x,y) is valid for
-- all delimiters so then the given point is inside of the triangle.
delimeters :: (Fractional a, Ord a) => (a,a) -> (a,a) -> (a,a) -> [(a -> a -> Bool)]  
delimeters a b c = [delimiter x y z | (x,y,z) <- [(a,b,c), (b,c,a), (a,c,b)]]
    where delimiter (x1,y1) (x2,y2) (cx,cy) = let a = (y1 - y2) / (x1 - x2)
                                                  b = y1 - (a * x1)
                                                in if cy > cx * a + b
                                                      then (\x y -> y > x * a + b)
                                                      else (\x y -> y < x * a + b)

-- Check if given the points a b c, the coordinates (x,y) is inside of the
-- triangle
triangleContains :: (Fractional a, Ord a) => (a,a) -> (a,a) -> (a,a) -> (a,a) -> Bool
triangleContains a b c (x,y) = and [delimiter x y | delimiter <- delimeters a b c]

-- Check if the origin, point (0,0), is inside of the triangle ABC
triangleContainsOrigin :: (Fractional a, Ord a) => ((a,a),(a,a),(a,a)) -> Bool
triangleContainsOrigin (a,b,c) = triangleContains a b c (0,0)

-- below is just parsing the file to compatible data to processing
-- ugly part :[
replace :: Eq a => a -> a -> [a] -> [a]
replace a b = map $ \c -> if c == a then b else c

parseLine :: String -> [Float]
parseLine s = map read $ words $ replace ',' ' ' s

parseTriangle :: (Fractional a, Ord a) => [a] -> ((a, a), (a, a), (a, a))
parseTriangle xs = let (x1:y1:x2:y2:x3:y3:[]) = xs
                    in ((x1,y1),(x2,y2),(x3,y3))

parse = parseTriangle . parseLine

main = do triangles <- readFile "p102_triangles.txt"
          print $ length $ filter triangleContainsOrigin $ map parse $ lines triangles

