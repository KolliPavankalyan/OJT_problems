'''2. Write a program in Python to remove duplicate elements form array without using
inbuilt function.'''

li = [10,22,12,22]
uniq_ele = []
for i in li:
    if i not in uniq_ele:
        uniq_ele.append(i)
print(uniq_ele)