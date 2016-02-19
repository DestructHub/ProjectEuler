// Copyright 2016 the DestructHub Authors. All rights reserved
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// created by Manoel Vilela

package main

import (
	"fmt"
	"math"
)

type Polynom struct {
	a, b, c float64
}

var P = Polynom{a: 3, c: 2}
var H = Polynom{a: 2, c: 1}
var B float64 = 1

func main() {
	lastTriangle := 285.0
	for {
		lastTriangle += 1
		t := (math.Pow(lastTriangle, 2) + lastTriangle) / 2
		p := (B + math.Sqrt(B+4*P.a*P.c*t)) / (2 * P.a)
		h := (B + math.Sqrt(B+4*H.a*H.c*t)) / (2 * H.a)

		if math.Floor(p) == p && math.Floor(h) == h {
			fmt.Printf("%.0f\n", t)
			break
		}
	}
}
