'''23. Print the following pattern :'''
                

#Approch 1:
n=int(input("enter the value of n: "))
for i in range(1,n):
        if i%2!=0:
            print((n-i-1)*" "+(str(i)+" ")*(i))
        else:
            print((n-i)*" "+(str(i)+" ")*(i))

for i in range(n,0,-1):
    print((n-i)*" "+(str(i)+" ")*(i))
















#Approch 2:

# n=int(input("enter the value of n: "))
# for i in range(1,n):

#     print((n-i)*" "+(str(i)+" ")*(i))

# for i in range(n,0,-1):
#     print((n-i)*" "+(str(i)+" ")*(i))
