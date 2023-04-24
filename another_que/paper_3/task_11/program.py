with open("another_que/paper_3/task_11/file1.txt") as file1:
    f = file1.readlines()
    f = f[::-1]
    print(f)
    for i in f:
        print(i,end="")