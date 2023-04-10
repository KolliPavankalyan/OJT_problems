'''. Read a given file and extract the integers from each line, concatenate all the
integers present in the same line and print the sum of all these integers. eg: <File content>
He is 32 yrs old and his son is 7 yrs old . She is 27 yrs old and her daughter is 2 yrs old .'''

with open("OJT/another_que/Paper_5/task_6/file.txt") as file:
    f = file.readlines()
    new_list = []
    for i in f:
        for j in i:
            if j.isnumeric():
                print(j)