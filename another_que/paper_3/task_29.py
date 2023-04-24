'''9. Write a function called interleave which accepts two iterables of any type and
returns a new iterable with each of the given items "interleaved" (item 0 from
iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).'''


iterator1 = [1,2,3,4,3,4]
iterator2 = [5,6,7,8,10,11]
list_a = []
minimum = 0
if len(iterator1)<len(iterator2):
    min = len(iterator1)
    
else:
    min = len(iterator2)
for i in range(min):
    list_a.extend([iterator1[i],iterator2[i]])
print(list_a)
