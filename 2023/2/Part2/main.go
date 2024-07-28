package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)


func getPower(input string) int {
	red := 0
	green := 0
	blue := 0

	game := strings.Split(input, ": ")[1]
	game = strings.ReplaceAll(game, ";", ",")
	var cubes []string = strings.Split(game, ", ")
	for _, cube := range cubes {
		split := strings.Split(cube, " ")
		amount, _ := strconv.Atoi(split[0])
		color := split[1]
		if color == "blue" && amount > blue {
			blue = amount
		}
		if color == "green" && amount > green {
			green = amount
		}
		if color == "red" && amount > red {
			red = amount
		}

	}
	return red * green * blue
}

func main() {

	result := 0

	file, _ := os.Open("2023/2/Part1/input.txt")

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input := scanner.Text()
		result += getPower(input)
	}

	fmt.Println(result) // 75561
}
