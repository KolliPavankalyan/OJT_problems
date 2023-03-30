'''18. Write sample code for reproducing the below errors and print the user defined messages with the use of exception handling concept 
IndexError, TypeError, AttributeError, ValueError '''

#IndexError:

# def index_Error(li):
#     length = len(li)
#     try:
#         print(li[length])
#     except IndexError as err:
#         print(err)
#         print("Out of index")
# index_Error([1,2,3,4,5])


#typeError

# def type_error(a,b):
#     try:
#         print(a+b)
#     except TypeError as err:
#         print(err) 
# type_error(5,"5")




# ValueError:
# def value_error():
#     try:
#         n = int(input("please enter num :"))
#     except ValueError as err1:
#         print(err1)
# value_error()

#AttributeError:
class MyClass:
    def __init__(self):
        self.my_attribute = "hello"
    def newError(self):
        pass
m = MyClass()
print(m.pavan)


# my_object = MyClass()
# print(my_object.nonexistent_attribute)



#indentaionError

# def identation_error():
#     try:
#         a = -10
#         if a>0:
#         print(a)
#     except IndentationError as ind:
#         print(ind)
# identation_error()

    





# def type_errors(a,b):
#     try:
#         if a<b:
#             print(a)
#     except TypeError:
#         print("enter correct type error")
#     except ZeroDivisionError:
#         print("print denominator is not zero")
#     except ValueError:
#         print("Enter correct value")

# type_errors(5,0)