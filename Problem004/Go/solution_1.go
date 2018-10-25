package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var MAX = 10000
	for i := 100; i < 1000; i++ {
		for j := 100; j < 1000; j++ {
			if i*j < MAX {
				continue
			}
			a := strconv.Itoa(i * j)
			b := reverse(a)
			if strings.Compare(a, b) == 0 {
				MAX = i * j
			}
		}
	}
	fmt.Println(MAX)
}

func reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}
