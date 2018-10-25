package main

import (
	"fmt"
	"math"
)

const NUM = 600851475143

var GrDiv = 1

func main() {
	for i := 3; float64(i) < math.Sqrt(float64(NUM)); i += 2 {
		if NUM%i == 0 && isPrime(uint64(i)) {
			GrDiv = i
		}
	}
	fmt.Println(GrDiv)
}

func isPrime(n uint64) bool {
	if n < 2 {
		return false
	} else if n == 2 {
		return true
	} else if n%2 == 0 {
		return false
	}

	for i := 3; float64(i) <= math.Sqrt(float64(n)); i = i + 2 {
		if n%uint64(i) == 0 {
			return false
		}
	}

	return true
}
