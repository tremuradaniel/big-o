# what is the big o of this function?

# l = ['nemo'] * 10
l = ['nemo'] * 1000

def findNemo(list):
    print(list[0])

findNemo(l) # O(1) -- constant time

def findNemo2(list): # O(2) -- constant time
    print(list[0])
    print(list[1])

# But we do not say that a constant big o is O(2), O(3), O(4), etc.
# we simplify and say that it is O(1) when it comes to  constant time
