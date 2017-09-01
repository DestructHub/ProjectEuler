// Copyright 2016 the DestructHub Authors. All rights reserved
// Use of this source code is governed by a MIT-style
// license that can be found in the LICENSE file.

package main

import (
	"fmt"
	"math"
)

func powMod(a float64, b float64, mod float64) float64 {
	var result float64 = 1
	a = math.Mod(a, mod)
	for i := 1.0; i <= b; i++ {
		result = math.Mod((a * result), mod)
	}

	return result
}

func main() {
	var answer float64 = 0
	var mod float64 = 1E10

	for i := 1.0; i <= 1000; i++ {
		answer = math.Mod(powMod(i, i, mod)+answer, mod)
	}

	fmt.Println(int(answer))
}
