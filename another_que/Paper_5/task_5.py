''' 5. From given list of numbers, create a list of square of prime numbers .
l1 = [1, 4, 6, 11,15, 24, 19, 25] '''


l1 = [1, 4, 6, 11,15, 24, 19, 25]
li = []
for i in l1:
    if i>1:
        prime = True
        for j in range(2,i):
            if i%j == 0:
                prime=False
        if prime:
            li.append(i**2)

print(li)
