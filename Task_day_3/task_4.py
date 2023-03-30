'''4. In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out
all the keys in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’.
Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as
its value.'''


dictinary = {'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu',}
list_keys = []
list_values = []
for k,v in dictinary.items():
    list_keys.append(k)
    list_values.append(v)
print(list_keys)
print(list_values)
if "Australia"  in list_keys:
    print(dictinary["Australia"])
else:
    print("NA")
    

    