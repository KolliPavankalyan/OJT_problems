def numnbers(num):
    for i in range(num):
        yield i
f = numnbers(10)
print(next(f))