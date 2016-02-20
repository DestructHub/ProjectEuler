// Copyleft 2016 the DestructHub Authors. All rights reserved
// Use of this source code is governed by a MIT
// license that can be found in the LICENSE file.

// solution for the problem 27 of Project Euler
// concurrent solution: take about 3.5~4 seconds (about 3x faster from python version)

package main

import (
	"fmt"
	"math"
)

const (
	limit    = 1000 // a, b limits to search
	nThreads = 16   // number of nThreads
)

type result struct {
	primes int
	a      int
	b      int
}

var (
	resultchan = make(chan result, nThreads) // used to get results concurrently
	memory     = make(map[int]bool)          // memory for primes numbers
)

// quadratic function generator
// n² + an + b
func quadratic(a, b int) func(int) int {
	return func(n int) int {
		return n*n + a*n + b
	}
}

// decorator workaround on Go
// check if the value was be computed before
// return if exists, else compute
func memo(f func(int) bool) func(int) bool {
	return func(n int) bool {
		if val, exists := memory[n]; exists {
			return val
		} else {
			return f(n)
		}
	}
}

// simple function
// to check if is a prime
func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for q := 2; float64(q) < math.Floor(math.Sqrt(float64(n)))+1; q++ {
		if n%q == 0 {
			return false
		}
	}

	return true
}

// func evaluation n² + an + b
// return the n primes generate without gaps
// between [0, n]
func evalFunc(f func(int) int) int {
	n := 0
	for {
		if memo(isPrime)(f(n)) {
			n += 1
		} else {
			break
		}
	}
	return n
}

// make concurrent evaluation
// of the equation whose have
// generate more primes
func worker(split int) {
	limitSplited := split * limit / nThreads
	a, b, nPrimes := 0, 0, 0
	for i := -limitSplited; i < limitSplited; i++ {
		for j := -limit; j < limit; j++ {
			if n := evalFunc(quadratic(i, j)); n > nPrimes {
				a, b = i, j
				nPrimes = n
			}
		}
	}

	resultchan <- result{nPrimes, a, b}
}

// receiver the results
// from workers
func receiver() (a int, b int, nPrimes int) {
	a, b, nPrimes = 0, 0, 0
	for i := 0; i < nThreads; i++ {
		result := <-resultchan
		if result.primes > nPrimes {
			a, b = result.a, result.b
			nPrimes = result.primes
		}
	}
	return a, b, nPrimes
}

func main() {
	for part := 1; part <= nThreads; part++ {
		go worker(part)
	}

	a, b, _ := receiver()
	fmt.Printf("%v\n", a*b)
}
