'''3. Write a function called interleave which accepts two iterables of any type and 
returns a new iterable with each of the given items "interleaved" (item 0 from iterable 1, then item 0 
from iterable 2, then item 1 from iterable 1, and so on). An assumption here that both iterables 
contain the same number of elements.'''


#Approach 1:

def interleave(iterable1, iterable2):
    new_list = []
    for i in range(len(iterable1)):
        new_list.extend([iterable1[i],iterable2[i]])
    return new_list       
print(interleave([1,2,3,5],[6,5,4,8]))



def interleave(iterable1, iterable2):
    new_list = []
    resul = list((zip(iterable1,iterable2)))
    print(resul)
interleave([1,2,3,1],[4,5,6,4])



