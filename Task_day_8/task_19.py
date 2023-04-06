'''19. Define a generator to print the numbers between o to n (including) which are divisible by 5 and should be even 
N = 20 
Output: 10 20 '''

def even_five(N):
    for i in range(1,N+1):
        if i%5==0 and i%2==0:
            yield i
N = int(input("Please enter number : "))
gen = even_five(N)
print(gen)
print(next(gen))
for i in gen:
    print(i, end=" ")