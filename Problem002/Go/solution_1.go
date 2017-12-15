package main

import "fmt"
import "time"

func p2(n int) int {
	sum, a, b, c := 0, 1, 1, 2 // c = a + b
	for c < n {
	        if n % 2 == 0 {
	  	        sum += c
	        }
		a = b + c
		b = c + a
		c = a + b
	}

	return sum
}

func main(){
    time.Sleep(3000 * time.Millisecond)
	fmt.Print(p2(4000000))
}
