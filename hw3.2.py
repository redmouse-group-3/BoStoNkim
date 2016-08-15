x = int(input("Введите число от 1 до 9: "))
def onethree(x):
    if 1 <= x <= 3:
        s = str(input("Введите строку: "))
        n = int(input("Введите число повторов строки: "))
        print((s+'\n')*n)

def foursix(x):
    if 4 <= x <= 6:
        m = int(input('Введите степень:'))
        print(x**m)

def sevennine(x):
    if 7 <= x <= 9:
        for i in range((x+1),(x+11)):
            print (i)
onethree(x)
foursix(x)
sevennine(x)
