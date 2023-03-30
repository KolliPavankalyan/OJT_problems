'''18. Write a python program where for every two hours it prints the pattern without using
sleep function
**********
********
******
***
*
'''

import time 

def func(num):
    while num>0:
        if num==4:
            num=num-1
            print("*"*num)
        
        else:
            print("*"*num)
        num=num-2

start_time = time.time()
interval = 10

while True:
    current_time = time.time()
    if current_time - start_time >= interval:
        func(10)
        start_time = current_time

