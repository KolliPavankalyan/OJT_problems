'''5. Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’, 
‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values associated 
with keys in alphabetically sorted order.'''

dict_A = {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh', 
'TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}

list_keys = sorted(list(dict_A.keys()))
list_values = []
for i in list_keys:
    list_values.append(dict_A[i])
print(list_values)