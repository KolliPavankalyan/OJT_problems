'''. Given a list of first 10 natural numbers, write a program to find the square of all even numbers 
and cube of all odd numbers and store them in another list'''

list_a = list(range(1,10))
even_a = [i for i in list_a if i%2==0]
even_d = [i for i in list_a if i%2!=0]
print(even_a,even_d)