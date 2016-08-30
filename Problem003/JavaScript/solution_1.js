'use strict'

const prime = num => {

	if(num == 1) {
		return 1;
	}

	let i;

	for(i = 2; i < num; i++) {
		if(num % i == 0) {
			num /= i;
		}
	}

	return i;
}

console.log(prime(600851475143));