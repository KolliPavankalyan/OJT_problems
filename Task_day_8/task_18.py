'''18. Write sample code for reproducing the below errors and print the user defined messages with the use of exception handling concept 
IndexError, TypeError, AttributeError, ValueError '''

#IndexError:

# def index_Error(li):
#     length = len(li)
#     try:
#         print(li[length])
#     except IndexError as err:
#         print("Index Error :{}".format(err))
# index_Error([1,2,3,4,5])


#typeError
def type_error(a,b):
    try:
        print(a+b)
    except TypeError as err:
        print("TypeError :{}".format(err)) 
type_error(5,"5")




# ValueError:
import math
# def value_error(n):
#     try:
#         print(math.sqrt(n))
#     except ValueError as err:
#         print("ValueError :{}".format(err)) 
# n = int(input("please enter num :"))
# value_error(n)



#AttributeError:
# try:
#     class MyClass:
#         def __init__(self):
#             self.my_attribute = "hello"
#         def newError(self):
#             pass
#     m = MyClass()
#     print(m.pavan)
# except AttributeError as err:
#     print("AttributeError :{}".format(err))

