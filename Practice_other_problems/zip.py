l1 = ["pavan","kalyan","kolli"]
l2 = [1,2,3]
l3 = ["a",'b','c']
new_list = []
for i in (zip(l1,l2,l3)):
    new_list.extend(i)
print(new_list)