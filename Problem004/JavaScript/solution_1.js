'use strict'

function is_palindrome(s){
    return s === s.split('').reverse().join('')
}

function find_max_palindrom(){
    max = 0
    for (i=100; i<999; i+=1){
        for (j=100; j<999; j+=1){
            if (is_palindrome(i*j + '') && i*j > max) {
                max = i*j;
            }
        }
    }
    return max;
}

console.log(find_max_palindrom())
