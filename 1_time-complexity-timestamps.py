from datetime import datetime

l = ['nemo'] * 10
# l = ['nemo'] * 10000

def findNemo(list):
    t0 = datetime.now().timestamp()
    for x in list:
        if (x == "nemo"):
            print("found nemo!")
    t1 = datetime.now().timestamp()
    print("Call to find nemo took:", t1 - t0, "seconds")

findNemo(l)

