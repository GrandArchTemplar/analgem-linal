class MyPolinom:
    # в i-ой ячейке массива хранится коэффициент при i-ой степени x
    def __init__(self, coefficients: list[float]):
        self.pl = coefficients

    def __str__(self):
        str = ""
        for i in range(len(self.pl))[::-1]:
            if self.pl[i] == -1:
                str += '-'
            elif self.pl[i] < 0:
                str += f"{self.pl[i]}"
            elif self.pl[i] > 0:
                str += f"+{self.pl[i]}" if i != len(self.pl)-1 else f"{self.pl[i]}"
            else:  # if i==0
                continue
            str += "x" * i
        return str


if __name__ == '__main__':
    print(MyPolinom([1, 2, 3, 0, 0, -1]))
