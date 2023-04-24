'''2. Write a decorator function that will record the number of times a function is
called. Your decorator function should be called record_calls and call_count
attribute that keeps track of the number of times it was called.
'''

def call_record(func):
    def wrapper(x):
        func(x)
        wrapper.call_count+=1
    wrapper.call_count =0
    return wrapper




@call_record
def main_func(x):
    print("hellon world")

main_func(10)
main_func(20)
print(main_func.call_count)