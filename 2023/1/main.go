package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func parseNumberFromStr(t string) int {
	var firstNumber string = ""
	var secondNumber string = ""

	for i := 0; i < len(t); i++ {
		var val = string(t[i])
		_, err := strconv.Atoi(val)
		if err != nil {
			continue
		}
		if firstNumber == "" {
			firstNumber = val
		}
		secondNumber = val
	}
	var combined string = firstNumber + secondNumber
	converted, err := strconv.Atoi(combined)
	if err != nil {
		panic(err)
	}
	return converted
}

func main() {
	file, err := os.Open("2023/1/input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var result int = 0
	for scanner.Scan() {
		text := scanner.Text()
		result += parseNumberFromStr(text)
	}
	fmt.Println(result)
}
