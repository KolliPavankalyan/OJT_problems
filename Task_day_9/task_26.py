'''26. Check sum of 2 numbers from given list which matches target value and returns the indexes of those numbers in the form of list. l1 = [ 7,8,2,3,6,9,2,8] Target = 14 O/p should be: [1,4] Note : We should not be using more than 1 loop. '''

li = [7,8,2,3,6,9,2,8]
target = 15

def first(li):
    for i in range(1,len(li)):
        a = li[0]
        b = li[i]
        if (a+b) == target:
            return [a,b]
    return first(li[1:])
a,b = (first(li))
print(li.index(a),li.index(b))
