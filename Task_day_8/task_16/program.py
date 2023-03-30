'''16. Let's consider there are two files, one file contains testnames, other file contains testnames and status for each one. Generate dictionary with key's as testname and 
value as status 
Input: 
File1.txt: 
test1 
test2 
File2.txt: 
test1-pass 
Output: 
test2-fail 
{ "test1" : "pass", "test2" : "fail"}'''



# f1 = open("Task_day_8/task_16/File1.txt",'r')
# key = f1.read()
# f1.close()
# f2 = open("Task_day_8/task_16/File2.txt","r")
# pair = f2.read()
# print(pair)


with open("Task_day_8/task_16/File1.txt",'r') as file1:
    key = (file1.read()).split()
    

with open("Task_day_8/task_16/File2.txt",'r') as file2:
    pair =file2.read()


key_val = [[j for j in i.split("-")] for i in pair.split()]

dict_A = {}

for i in key:
    for j in key_val:
        if i==j[0]:
            dict_A[i]=j[1]
print(dict_A)

#     dict_A[key[i]]=key_val[i][0]
# print(dict_A)
