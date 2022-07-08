# write 2 functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

def findFactorialRecursive(no):
    if (no > 1):
        return no * findFactorialRecursive(no - 1)
    else:
        return 1
    
    

def findFactorialIterative(no):
    result = 1
    while no > 1:
        result *= no
        no -= 1
    print("result of findFactorialIterative:", result)


print("findFactorialRecursive result:", findFactorialRecursive(5))
findFactorialIterative(5)