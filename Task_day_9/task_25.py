'''25. Write a function that employs regular expressions to ensure the password given to the function is strong. A strong password is defined as follows: -at least eight characters long -contains one uppercase character -contains one lowercase character -has at least one digit -has at least one special character '''


import re

def strong_pass(string):
    
    if len(string)>=8:
        if re.search(r'[A-Z]',string):
            if re.search(r'[a-z]',string):
                if re.search(r'\d',string):
                    if re.search(r'[!@#$^&*()+*/]',string):
                        return True
    return False

print(strong_pass("Pavhdb56362"))



# def is_password_strong(password):
#     # At least eight characters long
#     if len(password) < 8:
#         return False
    
#     # Contains one uppercase character
#     if not re.search(r'[A-Z]', password):
#         return False
    
#     # Contains one lowercase character
#     if not re.search(r'[a-z]', password):
#         return False
    
#     # Has at least one digit
#     if not re.search(r'\d', password):
#         return False
    
#     # Has at least one special character
#     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
#         return False
    
#     # All criteria met
#     return True