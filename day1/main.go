package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	content := readNumbers("input.txt")
	
	var content_p1 []int
	for _, x := range content {
        content_p1 = append(content_p1, calculate_fuel(x,false))  
	}
	var content_p2 []int
	for _, x := range content {
        content_p2 = append(content_p2, calculate_fuel(x,true))  
	}
	
	sum1 := 0
	sum2 := 0
	for i := 0; i < len(content_p1); i++ {
		sum1 = sum1+ content_p1[i]
		sum2 = sum2+ content_p2[i]
	}
	{
		fmt.Println("--- Part One ---")
		fmt.Println(sum1)
	}

	{
		fmt.Println("--- Part Two ---")
		fmt.Println(sum2)
	}
}

func calculate_fuel(mass int, recursive bool) int{
	result := mass/3 - 2
	if recursive {
		fuel := result
        for ((int(fuel/3)-2)>0){
			fuel= int(fuel/3)-2
            result+= fuel
		}
	}
	return result
}
func readNumbers(filename string) []int {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)

	var numbers []int
	for scanner.Scan() {
		numbers = append(numbers, toInt(scanner.Text()))
	}
	return numbers
}

func toInt(s string) int {
	result, err := strconv.Atoi(s)
	check(err)
	return result
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}