'''6. Write a program to extract the words starting with lowercase letter present in the list. [‘Nissan’, 
‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]'''

list_of_cars = ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']
final = []
for i in (list_of_cars):
    if i[0].islower():
        final.append(i)
        
print(final)