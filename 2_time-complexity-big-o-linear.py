# what is the big o of this function?

# l = ['nemo'] * 10
l = ['nemo'] * 10000

def findNemo(list):
    for x in list:
        if (x == "nemo"):
            print("found nemo!")

findNemo(l) # O(n) -- linear time

