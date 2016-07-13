string = ''
sep = str(input('Введите ваш разделитель: '))
list1 = string.split(sep)
z = list1[0]
x = ''
for i in list1:
    if len(z) > len(i):
        x = i
print(x)
