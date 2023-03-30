'''5. Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’,

‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values associated

with keys in alphabetically sorted order.'''

dictionary  = {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}
dictionary1 = sorted(dictionary.keys())
values = []
for i in dictionary1:
    values.append(dictionary[i])
print(dictionary1)
print(values)