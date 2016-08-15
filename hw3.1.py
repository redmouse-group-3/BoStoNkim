x = int(input('Введите число от 1 до 9:'))
if x >= 1 and x <= 3:
    s = str(input('Введите любую строку:'))
    n = int(input('Введите число повторов:'))
    print(s*n)
elif x >= 4 and x <= 6:
    m = int(input('Введите степень:'))
    print(x**m)
elif x >= 7 and x <= 9:
    list1 = [i for i in range((x+1),(x+10))]
    print (list1)
else:
    print('Ошибка ввода')
