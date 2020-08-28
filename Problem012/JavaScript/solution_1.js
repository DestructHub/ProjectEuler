"use strict"

function checkPrime(input, list) {
    for (let i = 0; i < list.length && list[i] < input ** 0.5; i++) 
        if (!(input % list[i])) return 0;
    return 1;
}

function getNumOfDivisor(input) {
    let prime_list = [2,3];
    let numDivisors = 1, counter = 1, k = 1;
    if (!(input % 2)) {
        input /= 2;
        while(!(input%2)) ++counter && (input /= 2);
        numDivisors *= ++counter; 
    }
    if (!(input % 3)) {
        (counter = 1) && (input /= 3);
        while(!(input % 3)) ++counter && (input /= 3);
        numDivisors *= ++counter;
    }
    while (6 * k - 1 <= input) {
        if (checkPrime(6 * k - 1, prime_list)) {
            prime_list.push(6 * k - 1);
            if (!(input % (6 * k - 1))) {
                (counter = 1) && (input /= (6 * k  -1));
                while (!(input % (6 * k - 1))) ++counter && (input /= (6 * k -1));
                numDivisors *= ++counter;
            }
        }
        if ((6 * k + 1) <= input && checkPrime(6 * k + 1, prime_list)) {
            prime_list.push(6 * k + 1);
            if (!(input % (6 * k + 1))) {
                (counter = 1) && (input /= (6 * k + 1));
                while (!(input % (6 * k + 1))) ++counter && (input /= (6 * k + 1));
                numDivisors *= ++counter;
            }
        }
        k++;
    }
    return numDivisors;
}

function getTriangleNumber() {
    let n = 45, numDivisors = 0;
    while (numDivisors <= 500) {
        (numDivisors = getNumOfDivisor(n * (n + 1)/2)) && ++n;
    }
    return ((n-1) * n / 2);
}

console.log(getTriangleNumber());
