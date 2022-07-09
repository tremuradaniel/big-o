"""
The Merge Sort algorithm is a sorting algorithm that is considered as an example of the divide and conquer strategy. 

So, in this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner. 
We can think of it as a recursive algorithm that continuously splits the array in half until it cannot be further divided. 
This means that if the array becomes empty or has only one element left, the dividing will stop, i.e. it is the base case to stop the recursion. 
If the array has multiple elements, we split the array into halves and recursively invoke the merge sort on each of the halves. 

Finally, when both the halves are sorted, the merge operation is applied. 
Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.
"""

import math
from operator import le   

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def merge (left, right):
    result = []

    indexLeft = 0
    indexRight = 0

    while indexLeft < len(left) and indexRight < len(right):
        if (left[indexLeft] < right[indexRight]):
            result.append(left[indexLeft])
            indexLeft += 1
        else:
            result.append(right[indexRight])
            indexRight += 1

    return result + left[indexLeft:] + right[indexRight:]


def mergeSort(list):
    if (len(list) == 1):
        return list

    middle = math.floor(len(list)/2)

    return merge(
        mergeSort(list[0:middle]),
        mergeSort(list[middle:])
    )




print(mergeSort(numbers))
