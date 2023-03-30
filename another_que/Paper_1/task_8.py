'''Create a dictionary where the key is an even number from the given list and the value
will be the occurrence of that element in the list. input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]'''

given_list = input("Please enter list of values").split()
given_list = [int(i) for i in given_list]

dict_A = {}
for i in given_list:
    if i in dict_A:
        dict_A[i]+=1
    else:
        dict_A[i]=+1

print(dict_A)
    