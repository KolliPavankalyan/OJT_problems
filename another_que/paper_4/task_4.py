'''4. Define a function which returns dictionary that stores the words and it's length from the given text 
text = "Be happy" 
Expected Output: {"Be":2,"happy":5} '''

text = "Be happy"
text_list = text.split()
dict_a ={}
for i in text_list:
    dict_a[i]=len(i)
print(dict_a)
