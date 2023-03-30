'''27. For any function, find out the arguments passed in the function using in-built python module and also explore on all other possible values we can get using the same python module. eg. def test(x1, x2, x3=10): pass Using the in-built python module, find all the arguments passed in the test function'''


import inspect

def func(x,y,z=10,**kwargs):
    print("----")
func(10,20,("a",2))

get_argument_details = inspect.getargspec(func)
print(get_argument_details.args)
print(get_argument_details.keywords)
print(get_argument_details.defaults)
print(get_argument_details.varargs)