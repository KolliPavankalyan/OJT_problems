from functools import reduce

def sub(a,b):
    return a-b
a = reduce(sub,[10,20,30,40])
print((a))