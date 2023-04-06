'''30. Create below 3 functions : - function 1 calculates sqrt - function 2 calculates cube

- function 3 calculates square Pass 50,00,000 as an integer argument which is 
going to be used as a range of integers. Call above 3 functions in parallel using below 3 ways :
1) Using multiprocessing 2) Using threading.thread 3) Using threadpoolexecutor 
Calculate the total time taken in each of these 3 ways .
 Share your observations/insights on the results obtained.'''


import time
#normal

t1 = time.perf_counter()
def sqrt(num):
    return num**(1/2)


def cube(num):
    return num**3

def square(num):
    return num**2

sqrt(5000000)
cube(5000000)
square(5000000)
t2 = time.perf_counter()
print(t2-t1)


#2.MultiThreading

# import threading
# t1 = time.perf_counter()
# def sqrt(num):
#     return num**(1/2)

# def cube(num):
#     return num**3

# def square(num):
#     return (num**2)

# th1 = threading.Thread(target=sqrt,args=[5000000])
# th2 = threading.Thread(target=cube,args=[5000000])
# th3 = threading.Thread(target=square,args=[5000000])

# th1.start()
# th2.start()
# th3.start()

# th1.join()
# th2.join()
# th3.join()
# t2 = time.perf_counter()
# print(t2-t1)


# Multiprocessing

# import multiprocessing

# def sqrt(num):
#     return (num**(1/2))

# def cube(num):
#     return num**3

# def square(num):
#     return (num**2)


# if __name__== "__main__":
#     m1 = time.perf_counter()
#     mp1 = multiprocessing.Process(target=sqrt,args=[5000000])
#     mp2 = multiprocessing.Process(target=cube,args=[5000000])
#     mp3 = multiprocessing.Process(target=square,args=[5000000])

#     mp1.start()
#     mp2.start()
#     mp3.start()

#     mp1.join()
#     mp2.join()
#     mp3.join()
#     m2 = time.perf_counter()
#     print(m2-m1)

# #Using threadpoolexecutor 
# from concurrent.futures import ThreadPoolExecutor
# m1 = time.perf_counter()
# def sqrt(num):
#     return (num**(1/2))

# def cube(num):
#     return num**3

# def square(num):
#     return (num**2)


# if __name__=="__main__":
#     with ThreadPoolExecutor(max_workers=3) as exe:
#         TP1 = time.perf_counter()
#         exe.submit(sqrt(5000000))
#         exe.submit(cube(5000000))
#         #exe.submit(square(5000000))
#         TP2 = time.perf_counter()
#     print(TP2-TP1)