'''19. Write a function which takes input string from the user as argument and the character also taken

by the user as the argument and remove all the occurences of that character from the string. Also if

the given character is not present in the string your function should raise the exception stating that

“Given character is not present in the string. Please try with a new one”.'''

#Approach 1:
def remove_char(string,char):
    if char not in string:
        raise Exception ("Given character is not present in the string. Please try with a new one")
    else:
        string = string.replace(char,"")
    return string

print(remove_char("pavan","a"))


# #Approach 2:
def check(string,char):
    try: 
        new_string = string.replace(char,"")
        if new_string==string:
            raise ValueError
        return new_string
        
    except ValueError:
        print("Given character is not present in the string. Please try with a new one")
    
    
out = (check("pavan","k"))
if out is not None:
    print(out)