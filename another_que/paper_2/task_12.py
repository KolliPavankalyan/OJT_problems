'''12. Write a method number_of_prime_numbers() which takes two input arguments num1 and 
num2 and should return the total number of prime numbers in the range. The numbers num1 and 
num2 are inclusive of the range. Also add all the numbers in an empty list and return the sum of the
list. So finally your function will return two things, first will be the count of prime numbers and the 
other will be the sum of all the prime numbers in the given range.'''

def number_of_prime_numbers(num1,num2):
    
    for i in range(num1,num2+1):
        prime = True
        for j in range(2,i):
            if i>1:
                if i%j==0:
                    prime= False
                    continue
        if prime:
            print(i)

number_of_prime_numbers(1,20)