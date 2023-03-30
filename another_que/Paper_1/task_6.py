'''6. Write a python program to right rotate a List by n
Enter position to rotate list item: 3
Sample input: [10, 20, 30, 40, 50, 60, 70]
Expected output: [50, 60, 70, 10, 20, 30, 40]'''

def right_rotate(list,num):
    return list[num:]+list[:num]
a = right_rotate([1,2,3,4,5,6],3)
print(a)