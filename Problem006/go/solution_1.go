package main

import "fmt"

func sumOfSquare(max int) int {
	result := 1
	for i := 2; i <= max; i++ {
		result += i * i
	}
	return result
}

func squareOfSum(max int) int {
	number := (max * (max + 1)) / 2
	return number * number
}

func main() {
	number := 100

	fmt.Println(squareOfSum(number) - sumOfSquare(number))
}
