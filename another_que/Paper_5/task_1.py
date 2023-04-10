'''. Write a program in Python to find second highest number in an integer array
without using inbuilt functions.'''

li = [74,12,47,23,23]
for i in range(len(li)):
    min = i
    for j in range(i+1,len(li)):
        if li[min]>li[j]:
            min=j
            
    li[i],li[min] = li[min],li[i]
print(li[-2])

