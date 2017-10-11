'use strict'

LIMIT = 4000000

even = (b) => b % 2 != 0

function sequence_generator(n, filter){
    a=1;
    b=1;
    array = [a, b];
    while (true){
        c = a;
        a = b;
        b = c + b;
        if (b > n) {
            break;
        }
        if (filter(b)){
            array.push(b);
        }
    }
    return array;
}

var solution = sequence_generator(LIMIT, even).reduce((a, b) => a + b, 0);
console.log(solution)
