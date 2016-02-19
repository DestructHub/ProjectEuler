// Copyright 2016 the DestructHub Authors. All rights reserved
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// created by Manoel Vilela

package main

import (
	"fmt"
	"math"
)

type polynom struct {
	a, b, c float64
}

var P = polynom{3, -1, -2}
var H = polynom{2, -1, -1}

func quadratic(a, b, c float64) float64 {
	return (-b + math.Sqrt(b*b-4*a*c)) / (2 * a)
}

func main() {
	lastTriangle := 285.0

	for {
		lastTriangle += 1
		t := (math.Pow(lastTriangle, 2) + lastTriangle) / 2
		p := quadratic(P.a, P.b, t*P.c)
		h := quadratic(H.a, H.b, t*H.c)

		if math.Floor(p) == p && math.Floor(h) == h {
			fmt.Printf("%.0f\n", t)
			break
		}
	}
}
