# assign list
l = [1, 2.0, 'have', 'a', 'geeky', 'day']
# assign string
s = 'geeky'
nl=list(map(str,l))
x=" ".join(nl)
print(x)
# check if string is present in the list
if x.find(s)!=-1:
	print(f'{s} is present in the list')
else:
	print(f'{s} is not present in the list')
