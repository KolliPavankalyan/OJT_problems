'''4. Define a function which returns dictionary that stores the words and it's length from the given text 
text = "Be happy" 
Expected Output: {"Be":2,"happy":5} '''


def count_word_length(given_string):
    given_string = given_string.split()
    dict_a = {}
    for i in given_string:
        dict_a[i]=len(i)
    return dict_a
print(count_word_length("Be happy"))