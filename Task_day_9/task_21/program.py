with open("Task_day_9/task_21/file1.txt","r") as file1:
    f1 = file1.read()
with open("Task_day_9/task_21/file2.txt","r") as file2:
    f2 = file2.read()
with open("Task_day_9/task_21/file3.txt","r") as file3:
    f3 = file3.read()

def check(*args):
    for i in args:
        if len(i)>=40:
            yield i

a = check(f1,f2,f3)
print(a)
for i in a:
    print(i)




