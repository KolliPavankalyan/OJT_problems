def generatir():
    yield 1
    yield 3
    yield 4
l = generatir()
for i in range(4):
    print(next(l))
