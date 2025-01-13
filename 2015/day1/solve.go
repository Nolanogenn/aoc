package main
import (
	"fmt"
	"os"
	s "strings"
)

func main() {
	dat, _ := os.ReadFile("in")
	pos := s.Count(string(dat), "(")
	neg := s.Count(string(dat), ")")
	fmt.Println("first sol: ", pos-neg)
	i := 0
	for pos, char := range string(dat){
		if char == 40 {
			i = i + 1
		} else if char == 41 {
			i = i - 1
		}
		if i == -1 {
			fmt.Println("second sol: ", pos)
			break
		}
	}
}
