'''18. Print the below rohmbus pattern according to the given number

for eg: given number is 4 then

o/p will be

1

212

32123

4321234

32123

212

1'''

num = 10

for i in range(1,num+1):
    output = ""
    for j in range(1,i+1):
        output += str(j)
        if j>1:
            output = str(j)+output
    print(output)
    if i==num:
        for i in range(num,1,-1):
            below = ""
            for j in range(1,i):
                below +=str(j)
                if j>1:
                    below=str(j)+below  
            print(below)

            
    
 
    