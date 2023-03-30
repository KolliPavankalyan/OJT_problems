# 2. Given a list of first 10 natural numbers, write a program to find the square of all even numbers
# and cube of all odd numbers and store them in another list

# Approch 1:


num = int(input("enter number :20"))
even_num = []
odd_num =[]
for i in range(1,num+1):
    if i%2==0:
        even_num.append(i**2)
    else:
        odd_num.append(i**3)
print(even_num)
print(odd_num)


# approch 2

num = 10
list_A = list(range(1,num+1))
even_num = [i**2 for i in list_A if i%2==0]
odd_num = [i**3 for i in list_A if i%2!=0]
print(even_num)
print(odd_num)