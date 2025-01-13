package main
import (
	"fmt"
	"os"
	"bufio"
	"regexp"
	"strconv"
)

func area(a [] string) int{
	l, _ := strconv.Atoi(a[0])
	w, _ := strconv.Atoi(a[1])
	h, _ := strconv.Atoi(a[2])
	s1 := l*w
	s2 := w*h
	s3 := h*l
	add := min(s1,s2,s3)
	return 2*s1 + 2*s2 + 2*s3 + add
}

func ribbons(a [] string) int{
	l, _ := strconv.Atoi(a[0])
	w, _ := strconv.Atoi(a[1])
	h, _ := strconv.Atoi(a[2])
	s1 := 2*(l+w)
	s2 := 2*(w+h)
	s3 := 2*(h+l)
	ribbon := min(s1,s2,s3)
	return ribbon+(l*w*h)
}

func main() {
	dat, _ := os.Open("in")
	scanner := bufio.NewScanner(dat)
	totalArea := 0
	totalRibbon := 0
	for scanner.Scan() {
		r, _ := regexp.Compile("[0-9]*")
		match := r.FindAllString(scanner.Text(),-1)
		totalArea = totalArea + area(match)
		totalRibbon = totalRibbon + ribbons(match)
	}
	fmt.Println("first solution: ", totalArea)
	fmt.Println("second solution: ", totalRibbon)
}
