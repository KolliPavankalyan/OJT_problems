'''1. Sort the below list without using inbulit function 
list_a = [1,3,4,-9,89]
'''

list_a = [1,3,4,-9,89]
for i in range(len(list_a)-1):
    min = i
    for j in range(i,len(list_a)):
        if list_a[min]>list_a[j]:
            min = j
    list_a[min],list_a[i]= list_a[i],list_a[min]
print(list_a)