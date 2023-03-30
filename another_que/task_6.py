'''Write a program to extract the words starting with lowercase letter present in the list. [‘Nissan’,
‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]
'''

given_list = input("enter the words:  ").split()
new_list = [i for i in given_list if i[0].islower()]
print(new_list)