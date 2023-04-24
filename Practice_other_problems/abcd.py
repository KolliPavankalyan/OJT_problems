num = 6
count =1
for i in range(1,num+1):
    space = " "*(num-i)
    out = ""
    for j in range(i):
        out += chr(64+count)+" "
        count+=1
    print(space+out)