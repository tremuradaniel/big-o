# what is the big O of this?
def challenge(input):
    a = 10 # O(1)
    a = 50 + 3; # O(1)

    for i in input:
        anotherFunc()  # O(n)
        t = True  # O(n)
        a += 1  # O(n)
    return a # O(1)

def anotherFunc():
    print('a')

# BIG(3 + 4n) --- in the end this will get simplified to O(n)

