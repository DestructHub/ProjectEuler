// Copyright 2017 the DestructHub Authors. (Manoel Vilela wrote this shit)

package main

import (
	"fmt"
	"math"
)

func numLength(n float64) int {
	if n < 10 {
		return 1
	}

	return 1 + numLength(n/10)
}

func main() {
	ndigits := 0
	for a := 1; a <= 9; a += 1 {
		for n := 1; n <= 21; n += 1 {
			if numLength(math.Pow(float64(a), float64(n))) == n {
				ndigits += 1
			}
		}
	}

	fmt.Println(ndigits)

}
