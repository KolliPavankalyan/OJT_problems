num = [10,20,30]
a = map(lambda x:x*5,num)
print(list(a))

num1 = [10,20,30,50,-10-50]
a = filter(lambda a:a>0,num1)
print(list(a))


num2 = [150,500,10,20,30,40,-88,-52,-55,-12]
a = map(lambda x:x*2,filter(lambda x:x>0,num2))
print(list(a))