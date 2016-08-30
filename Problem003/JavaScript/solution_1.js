'use strict'

const prime = num => {

	let i;

	for(i = 2; i < num; i++) {
		if(num % i == 0) {
			num /= i;
		}
	}

	return i;
}

console.log(prime(600851475143));