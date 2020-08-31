"use strict";

function getReducedFactorial() {
    let prod = 1n, numOfTwo = 0, numOfFive = 0, num, sum = 0n;
    for (let i = 2; i <= 100; i++) {
        num = i;
        while (!(num % 2) && num >= 2) (num = Math.floor(num / 2)) && ++numOfTwo;
        while (!(num % 5) && num >= 5) (num = Math.floor(num / 5)) && ++numOfFive;
        prod *= BigInt(num);
    }
    prod *= BigInt((numOfTwo > numOfFive) ? 2 ** (numOfTwo - numOfFive) : 5 ** (numOfFive - numOfTwo));
    while (prod) (sum += prod % 10n) && (prod = prod / 10n);
    return sum;
}

console.log(parseInt(getReducedFactorial()));