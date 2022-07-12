calculations = 0

def fibonacci(n):
    global calculations 
    calculations += 1
    if (n < 2):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci simple ", fibonacci(12))
print("fibonacci simple calculations ", calculations)


calculations = 0

def fibonacci2(n):
    global calculations
    combinations = {}
    # works with the help of a closure function
    def fib(n):
        global calculations
        calculations += 1
        if n in combinations:
            return combinations[n]
        else:
            if (n < 2):
                return n
            combinations[n] = fib(n-1) + fib(n-2)
            return combinations[n]
    return fib(n)
    
    
    
print("fibonacci memoization ", fibonacci2(12))
print("fibonacci memoization calculations ", calculations)