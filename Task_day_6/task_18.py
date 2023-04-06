'''18. Create your own exception.'''

def exceptionError(num):
    try:
        if num >= 0:
            print("This is possitive number")
        else:
            raise ValueError
    except ValueError:
        print("please enter positive number")

exceptionError(8)