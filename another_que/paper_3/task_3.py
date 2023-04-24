'''. Write a function called interleave which accepts two iterables of any type and
returns a new iterable with each of the given items "interleaved" (item 0 from
iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on). An
assumption here that both iterables contain the same number of elements.
'''

def interleave(list1,list2):
    print(list(zip(list1,list2)))
interleave([1,2,3,4],[5,6,7,8])
