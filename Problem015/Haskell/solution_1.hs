{--
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
-}

main :: IO ()
main = print $ div (fat 40) ((fat 20)^2)
	     where fat = (\x -> product [1..x])