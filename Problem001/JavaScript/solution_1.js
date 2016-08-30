'use strict'

const sumAllMultiples = limit => {
	let sum = 0

	for(let i = 0; i < limit; i++) {
		if(i % 3 == 0 || i % 5 == 0) {
			sum += i;
		}
	}

	return sum;
}

console.log(sumAllMultiples(1000));