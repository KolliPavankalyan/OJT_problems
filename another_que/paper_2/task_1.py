'''1. Write a program to reverse a number without using any inbuit function.'''

num = int(input())
out = 0
if num>0:
    num = num
elif num<0:
    out = -0
    string = str(num)[1:]
    num = int(string)
    

while num != 0:
    remander = num%10
    out = (out*10)+remander
    num = num//10

print(out)

# num = int(input("Enter a num  :"))
# out = 0
# def reverse(num):
#     while num != 0:
#         remander = num%10
#         out = (out*10)+remander
#         num = num//10
#     return out
# if num > 0:
#     print(reverse(num))
# elif num<0:
#     string = str(num)
#     num = int(string[1:])
#     print(num)
#     print(reverse(num))


