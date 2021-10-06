package main

import "fmt"

func smallest_multiple(number int) int {
	for result := 2; ; result++ {
		found := true
		for i := 2; i <= number; i++ {
			if result%i != 0 {
				found = false
				break
			}
		}
		if found {
			return result
		}
	}
}

func main() {
	fmt.Println(smallest_multiple(20))
}
