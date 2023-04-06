def remove_nagatives(num):
    if num>0:
        return True
    else:
        return False
    
a = filter(remove_nagatives,[1,5,-52,50,89])
print(list(a))
