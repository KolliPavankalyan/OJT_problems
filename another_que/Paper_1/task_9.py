'''Write a function swap_element that contains two args which will be the position of
elements present in the list. The function must swap the elements present in those
positions.
'''

def swap(given_list,arg_1,arg_2):
    given_list[arg_1],given_list[arg_2] = given_list[arg_2],given_list[arg_1]
    return given_list
print(swap([1,2,3,410,20,10],1,5))
