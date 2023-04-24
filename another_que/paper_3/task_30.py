'''30. Convert each list element to a key-value pair.
ex:
Input : test_list = [2323, 82, 129388, 95]
Output : {23: 23, 8: 2, 129: 388, 9: 5}'''
input_list = [2323, 82, 129388, 95]
dict_A = {}
for i in input_list:
    i = str(i)
    dict_A[int(i[:len(i)//2])]=int(i[(len(i)//2):])
print(dict_A)