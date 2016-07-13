string = ''
list1 = string.split(' ')
z = 0
x = ''
for i in list1:
    if len(i) > z:
        z = len(i)
        x = i
print(x)

