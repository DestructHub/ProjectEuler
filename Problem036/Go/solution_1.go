package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}
	return true
}

var binary = func(i int64) string { return strconv.FormatInt(i, 2) }

func main() {
	number := 0
	for i := 0; i < 1000000; i++ {
		if isPalindrome(strconv.Itoa(i)) && isPalindrome(binary(int64(i))) {
			number += i
		}
	}
	fmt.Println(number)
}
