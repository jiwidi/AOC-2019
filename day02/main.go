package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	content := readFile("input.txt")

	var program []int
	for _, value := range strings.Split(content, ",") {
		program = append(program, toInt(value))
	}

	// Solve part1
	program_p1 := make([]int, len(program))
	copy(program_p1, program)
	program_p1[1]=12
	program_p1[2]=2	
	var content_p1 []int = int_code(program_p1)
	{
		fmt.Println("--- Part One ---")
		fmt.Println(content_p1[0])
	}
	//Solve part2
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			program_p2 := make([]int, len(program))
			copy(program_p2, program)
			program_p2[1]=noun
			program_p2[2]=verb
			var content_p2 []int = int_code(program_p2)
			if content_p2[0]==19690720{
				fmt.Println("--- Part Two ---")
				fmt.Println(100*noun+verb)
			}
		}
	}
}

func int_code(code []int) []int{
	for i := 0; i+4 < len(code); i++ {
		if code[i]==1{
			code[code[i+3]] = code[code[i+1]]+code[code[i+2]]
			i+=3
		} else if code[i]==2{
			code[code[i+3]] = code[code[i+1]]*code[code[i+2]]
			i+=3
		}
		
	}
	return code
}
func readFile(filename string) string {
	bytes, err := ioutil.ReadFile(filename)
	check(err)
	return strings.TrimSpace(string(bytes))
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