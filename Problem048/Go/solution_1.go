// Copyright 2016 the DestructHub Authors. All rights reserved
// Use of this source code is governed by a MIT-style
// license that can be found in the LICENSE file.

package main

import (
	"fmt"
	"math"
)

func main() {
	var answer float64

	for i := 1.0; i <= 1000; i++ {
		fmt.Println(math.Pow(i, i))
		answer += math.Mod(math.Pow(i, i), 1e10)
	}

	fmt.Println(answer)
}
