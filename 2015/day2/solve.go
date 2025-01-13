package main
import (
	"fmt"
	"os"
	"bufio"
)

func main() {
	dat, _ := os.Open("in")
	scanner := bufio.NewScanner(dat)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
