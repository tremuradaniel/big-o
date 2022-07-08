# Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
# The array is virtually split into a sorted and an unsorted part. 
# Values from the unsorted part are picked and placed at the correct position in the sorted part.

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(nums):
    results = []
    for n in range(len(nums)):
        if (len(results) == 0):
            results.append(nums[n])
            continue
        index = 0
        i = len(results) - 1
        while i >= 0:
            if (nums[n] > results[i]):
                index = i + 1
                break
            i -= 1

        results.insert(index, nums[n])
            
    return results


print(insertionSort(numbers))

        
        