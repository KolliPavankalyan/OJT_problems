'''1. Sort the below list without using inbuilt function 
| = [2,3,-5,-7,9,4,6,-1,-8,0] '''

#Approch 1:

# def Sort_list(li):
#     li = [int(i) for i in li.split()]
#     for i in range(len(li)):
#         for j in range(i+1,len(li)):
#             if li[i]>li[j]:
#                 li[i],li[j]= li[j],li[i]
#     return li

# print(Sort_list(input("Please Enter list of numbers")))

#Approch 2:

def sort_list(li):
    li = [int(i) for i in li]
    for i in range(len(li)):
        min_val = i
        for j in range(i+1,len(li)):
            if li[min_val] > li[j]:
                min_val = j
        li[min_val],li[i] = li[i],li[min_val]
    return li
li = input("Please Enter lidt of numbers  :").split()
print(sort_list(li))
