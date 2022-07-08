# The selection sort algorithm sorts an array by repeatedly finding the minimum element
#  (considering ascending order) from unsorted part and putting it at the beginning.

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

def selectionSort(lista):
    n = 0
    while n < len(lista) - 1:
        tempL = lista[n:]
        smallestNo = tempL[0]
        for k,_ in enumerate(tempL):
            if (k+1 < len(tempL)):
                smallestNo = smallestNo if smallestNo < tempL[k+1] else tempL[k+1]
        lista.remove(smallestNo)
        lista.insert(n, smallestNo)
        n += 1

    return lista

print(selectionSort(numbers))


# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]
 
# Traverse through all array elements
for i in range(len(A)):  
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j    
    # Swap the found minimum element with
    # the first element  
    A[i], A[min_idx] = A[min_idx], A[i]
 
    # Driver code to test above
    print ("Sorted array")
    for i in range(len(A)):
        print("%d" %A[i]),