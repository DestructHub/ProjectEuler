{-- Author: Manoel Vilela

Time: 0.003s (3ms) @ Intel E7400 3.5Ghz

The biggest solution for this problem is the mathematical background.
The source code written here is just a straight forward evaluation of it.

Well, to beginning this lets make clear the problem:

:: How many n-digit positive integers exist which are also an nth power?

So we are looking a arbitrary a^n = k whose k has length n.
A arbitrary number k has the length n when this constraint is True:

10^(n-1) <= k < 10^n

Let's take a example. For n <- 4 all the n-digits numbers are between
that bounds: 10^3 <= k < 10^4 <=> 1000 <= k < 10000

Which seems true. For this be very trivial, I'll not write a proof here.
But which the values possible for `a` and `n`?

To start, let's look with `a` for k = a^n (more easy):

1 = 1^1
2 = 2^1
3 = 3^1
...
9 = 9^1
but 10 = 10^1, length "10" == 2 and n == 1, so `a` cannot be 10.

Looking at this and the constraint k < 10^n, if we write k as a^n, which means
a^n < 10^n, then so the biggest integer for which this is True is when a = 9.
9^n < 10^n, any a > 9 this statement is false.

So `a` is on the interval [1,9]

In another case, which values `n` can assume? Let's look to this
inequality: 10^(n-1) <= a^n

What the max value that n can assumes? Let's assume `a` for the biggest
value possible (9) and the case when this statement is a equality, so then:

10^(n - 1) = 9^n

log(10^(n-1)) = log(9^n)    {logarithm of base 10 on both sides}
(n-1)*log(10) = n * log(9)  {logarithm theorem log(a^b) = a * log(a)}
n - 1 = n * log(3^2)        {log(10)=1 and 9 = 3^2}
n -1 = n * 2*log(3)         {again logarithm theorem of power}
n - n*2*log(3) = 1          {sum 1 - 2*log(3) on both sides}
n(1 - 2*log(3)) = 1         {distributive law of multiplication}
n = 1/(1 - 2*log(3))        {divide both sides for (1 - 2*log(3))}
n ~= 21                     {evaluation for n as integer}

That means so we need look for a <- [1..9] and n <- [1..21].
The most simplest implementation on Haskell is given below.

--}

main :: IO()
main = print $ length [x | a <- [1..9], n <- [1..21],
                           let x = a^n,
                           n == length (show x)]
