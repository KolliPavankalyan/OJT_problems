"""16. Write a program to multiply two given number without using “*” operation and any in built
function"""

def multiply(num1, num2):
    result = 0
    if num1 == 0 or num2 == 0:
        return 0
    
    elif num1 > 0 and num2 > 0:
        for i in range(num2):
            result += num1
        return result
    
    elif num1 > 0 and num2 < 0:
        for i in range(abs(num2)):
            result -= num1
        return result
    
    elif num1 < 0 and num2 > 0:
        for i in range(abs(num1)):
            result -= num2
        return result
    
    elif num1 < 0 and num2 < 0:
        for i in range(abs(num1)):
            result += abs(num2)
        return result


print(multiply(-10,-4))


