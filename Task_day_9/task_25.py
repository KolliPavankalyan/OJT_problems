'''25. Write a function that employs regular expressions to ensure the password given to the function is strong. A strong password is defined as follows: -at least eight characters long -contains one uppercase character -contains one lowercase character -has at least one digit -has at least one special character '''


import re

def strong_password(string):
    
    if len(string)>=8:
        if re.search(r'[A-Z]',string) and re.search(r'[a-z]',string) and re.search(r'\d',string) and re.search(r'[!@#$^&*()+*/]',string):
            return True
    return False

print(strong_password("avhdb56362@"))
















# def strong_password(string):
    
#     if len(string)>=8:
#         if re.search(r'[A-Z]',string):
#             if re.search(r'[a-z]',string):
#                 if re.search(r'\d',string):
#                     if re.search(r'[!@#$^&*()+*/]',string):
#                         return True
#     return False

# print(strong_password("Pavhdb56362"))
