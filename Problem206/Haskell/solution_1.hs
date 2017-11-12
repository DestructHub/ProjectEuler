{-- Author: Manoel Vilela

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

--}

{--
Some thoughts:

As n² = 1_2_3_4_5_6_7_8_9_0 terminates with 0, so then n as well terminates
with 0. But any number terminated with 0 and squared will have two zeros.
(x * 10)^2 = 100 * x^2

So the number we are looking has the form: 1_2_3_4_5_6_7_8_900

Ignoring the last two zeros we have 1_2_3_4_5_6_7_8_9.
A number terminated with 9. So the square root of this must
terminated with a digit 7 or 3 (because 3² => 9 and 7² => 49).

That way we just look for n values whose the last digits is
3 or 7.

The max value to check is sqrt(19293949596979899)
The min value to check is sqrt(10203040506070809)

Range of almost 5 millions. But using numbers terminated with 3
or 7 will cut this to 1/5. So we'll check, in the worst case,
1 million of numbers. (much better to check 1 billion using brute-force)
--}


-- check if n match on the mask 1_2_3_4_5_6_7_8_9
numFitness :: Integer -> Bool
numFitness n = and [a == b | (a,b) <- zip ['1'..'9'] num]
  where num = [str !! k | k <- filter even [0..length str]]
        str = show n

-- For some reason looking for the maxValue to minValue we got a AWESOME
-- optimization on final performance
magicNum :: Integer
magicNum = (* 10) $ head $ filter (numFitness . \x -> x * x) nums
  where minv = floor $ (sqrt 10203040506070809)/10
        maxv = floor $ (sqrt 19293949596979899)/10
        nums = concatMap (\n -> [n*10 + 3, n*10 + 7]) [maxv,maxv-1..minv]

main :: IO()
main = print magicNum
