'''4. In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out 
all the keys in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’. 
Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as 
its value.'''


dict_a = {'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu','Australia':'capita'} 
list_keys = []
list_values = []
for k,v in dict_a.items():
    list_keys.append(k)
    list_values.append(v)
if "Australia" in list_keys:
    print("hi")
else:
    print("NA")