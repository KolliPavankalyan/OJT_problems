''''''


def isValid(s):
    stack = []
    dict = {"(":")","{":"}","[":"]"}
    for char in s:
        if char in dict.keys():
            stack.append(dict[char])
            print(stack)
        elif len(stack) == 0 or stack[-1] != char:
            return False
        else:
            stack.pop()
    return len(stack) == 0
print(isValid("()[]{}"))
print(isValid("({[)]"))
print(isValid("{()}"))