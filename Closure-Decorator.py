def checkValue(func):
    def verifyValue(base, heigth):
        if base < 5:
            print("[Alas dibawah 5, maka alas menjadi 5]")
            base = 5
        if heigth < 5:
            print("[Tinggi dibawah 5, maka tinggi menjadi 5]")
            heigth = 5
        return func(base, heigth)
    return verifyValue


@checkValue
def triangleArea(base, heigth):
    luas = 1/2 * base * heigth
    print("Luas Segitiga \t: ",luas)


triangleBase = int(input("Alas Segitiga \t: "))
triangleHeigth = int(input("Tinggi Segitiga : "))

triangleArea(triangleBase, triangleHeigth)