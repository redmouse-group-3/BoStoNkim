list1 = [2,3,6,9,9,11,2,4,8]
def hw34(x):
    list2 = []
    p = 1
    for i in x:
        list2.append(i**p)
        p = i
    print (list2)

hw34(list1)
        
