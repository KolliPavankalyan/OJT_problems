'''4. Write to_celsius function that accepts a temperature in Fahrenheit as input and returns a temperature in Celsius.'''\


#Approach 1:

# def Fahrenheit_to_celsius(temp):
#     if temp[-1]=="F":
#         con_tem = float(temp[:len(temp)-1])
#         Fahrenheit = (con_tem - 32) * (5/9)
#         return Fahrenheit

# # enter_celsius = input("Enter the temparature in Fahrenheit  :") 
# print(round(Fahrenheit_to_celsius("500F"),5))


#Approach 2:

def Fahrenheit_to_celsius(temp):
    if temp[-1]=="F":
        con_tem = float(temp[:len(temp)-1])
        return (con_tem - 32) * (5/9)
    elif temp[-1] != "F" and temp[-1].isdigit():
        return (float(temp)-32) * (5/9)
    
print(Fahrenheit_to_celsius("100"))
print(Fahrenheit_to_celsius("100F"))

