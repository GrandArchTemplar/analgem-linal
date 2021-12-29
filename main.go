package main

import (
	"fmt"
	"math"
)

func sqrEq(x, y float64) (float64, float64) {
	discriminant := x*x - 4*y
	x1 := (x + math.Sqrt(discriminant)) / 2
	x2 := (x - math.Sqrt(discriminant)) / 2
	return x1, x2
}

func main() {
	var a, b, c, d, e, f float64
	fmt.Print("A: ")
	if _, err := fmt.Scanln(&a); err != nil {
		panic(err)
	}
	fmt.Print("B: ")
	if _, err := fmt.Scanln(&b); err != nil {
		panic(err)
	}
	fmt.Print("C: ")
	if _, err := fmt.Scanln(&c); err != nil {
		panic(err)
	}
	fmt.Print("D: ")
	if _, err := fmt.Scanln(&d); err != nil {
		panic(err)
	}
	fmt.Print("E: ")
	if _, err := fmt.Scanln(&e); err != nil {
		panic(err)
	}
	fmt.Print("F: ")
	if _, err := fmt.Scanln(&f); err != nil {
		panic(err)
	}
	b, d, e = b/2, d/2, e/2

	tau := a + c
	delta := a*c - b*b
	bigDelta := a*c*f + 2*d*b*e - d*d*c - a*e*e - f*b*b
	k := a*f + c*f - d*d - e*e
	if a*a+b*b+c*c == 0 {
		if d*d+e*e == 0 {
			if f == 0 {
				fmt.Println("Все пространство")
			} else {
				fmt.Println("Пустое множество")
			}
		} else {
			fmt.Println("Прямая")
		}
	} else if delta > 0 {
		if bigDelta == 0 {
			fmt.Println("Точка")
			return
		} else if tau*bigDelta > 0 {
			fmt.Println("Мнимый эллипс")
		} else if tau*bigDelta < 0 {
			lambda1, lambda2 := sqrEq(tau, delta)
			if math.Abs(lambda1) > math.Abs(lambda2) {
				lambda1, lambda2 = lambda2, lambda1
			}
			a2 := -bigDelta / (lambda1 * delta)
			b2 := -bigDelta / (lambda2 * delta)
			fmt.Printf("Эллипс: %f * x^2 + %f * y2 = 1 \n", 1/a2, 1/b2)
			fmt.Println("Линейный эксцентриситет с = ", math.Sqrt(a2-b2))
		}
	} else if delta < 0 {
		if bigDelta == 0 {
			fmt.Println("Две пересекающиеся прямые")
		} else if bigDelta != 0 {
			lambda1, lambda2 := sqrEq(tau, delta)
			if lambda2*bigDelta > 0 {
				lambda1, lambda2 = lambda2, lambda1
			}
			a2 := -bigDelta / (lambda1 * delta)
			b2 := math.Abs(-bigDelta / (lambda2 * delta))
			fmt.Printf("Гипербола: %f * x^2 - %f * y2 = 1 \n", 1/a2, 1/b2)
			fmt.Println("Линейный эксцентриситет с = ", math.Sqrt(a2+b2))
		}
	} else if delta == 0 {
		if bigDelta == 0 {
			if k < 0 {
				fmt.Println("Две параллельные прямые")
			} else if k > 0 {
				fmt.Println("Две мнимые параллельные прямые")
			} else if k == 0 {
				fmt.Println("Две совпадающие прямые")
			}
		} else if bigDelta != 0 {
			lambda1, lambda2 := sqrEq(tau, delta)
			if lambda2 == 0 {
				lambda1, lambda2 = lambda2, lambda1
			}
			p := math.Sqrt(-bigDelta / (tau * tau * tau))
			fmt.Printf("Парабола: y^2 = 2 * %f * x\n", p)
			fmt.Println("Фокальный параметр p = ", p)
		}
	}
}
