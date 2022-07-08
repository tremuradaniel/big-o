# Given a number N return the index value of the Fibonacci sequence

def fibonacciIterative(no):
    l = []

    while (no >= 0): # O(n)
        if (len(l) < 2):
            l.append(len(l))
        else:
            l.append(l[-1] + l[-2])

        no -= 1

    return l[-1]

def fibonacciRecursive(n): # O(2^n)
    if (n < 2):
        return n
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

print(fibonacciIterative(3))
print(fibonacciIterative(8))
print(fibonacciIterative(12))
print("-")
print(fibonacciRecursive(3))
print(fibonacciRecursive(8))
print(fibonacciRecursive(12))
# this would take a really long time...
# print(fibonacciRecursive(40))