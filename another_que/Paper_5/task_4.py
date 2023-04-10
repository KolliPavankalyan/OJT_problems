'''4. Write Python program to perform left rotation of array elements '''

li = [12,22,32,22,75]
pos = int(input("Please enter number  :"))
pos = pos%len(li)
print(li[pos:]+li[:pos])