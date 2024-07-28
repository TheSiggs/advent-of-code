package main

import (
	"fmt"
	"strings"
    "strconv"
    "os"
    "bufio"
)

/*
The Elf would first like to know which games would have been possible if
the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

Total: 8 (1 + 2 + 5)
*/

// Constraints
var contraints = map[string]int{
    "red": 12,
    "green": 13,
    "blue": 14,
}

func validateGame(input string) int {
    var pass bool = true
    gameSplit := strings.Split(input, ": ")
    gameName := gameSplit[0]
    gameId := strings.Split(gameName, " ")[1]
    id, _ := strconv.Atoi(gameId)
    game := gameSplit[1]
    sets := strings.Split(game, "; ")
    for _, set := range sets {
        cubes := strings.Split(set, ", ")
        for _, cube := range cubes {
            split := strings.Split(cube, " ")
            amount, _ := strconv.Atoi(split[0])
            color := split[1]
            if amount > contraints[color] {
                pass = false
            }
        }

    }
    if pass {
        return id
    }
    return 0
}

func main() {
    var input string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    file, _ := os.Open("2023/2/input.txt")  

    defer file.Close() 

    scanner := bufio.NewScanner(file) 
    result := 0 
    for scanner.Scan() {
       input = scanner.Text() 
       result += validateGame(input)
    }

    fmt.Println(result)
    if result != 2795 {
        panic("Wrong result!")
    }
}
