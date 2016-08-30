'use strict'

const sumAllMultiples = limit => Array(limit).fill().map((_, i) => i).filter(number => number % 3 == 0 || number % 5 == 0).reduce((total, number) => total + number)

console.log(sumAllMultiples(1000))