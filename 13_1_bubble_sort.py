list1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
list2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(l):
    r = []
    lLen = len(l)
    while len(r) != lLen:
        for k, n in enumerate(l):
            if (k+2 > len(l)):
                break
            if n > l[k+1]:
                l[k] = l[k+1]
                l[k+1] = n

        r.insert(0, l[-1])
        l.pop(-1)
    
    return r

def bubbleSort2(l): # inst
    length = len(l)
    i = 0
    while i < length:
        j = 0
        while j < length:
            if (j+2 > length):
                break
            if (l[j] > l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1]= temp
            j += 1
        i += 1

    return l

print(bubbleSort(list1))
print(bubbleSort2(list2))
    
