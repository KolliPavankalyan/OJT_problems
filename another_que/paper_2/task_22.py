'''22. Find the palindrome words with the count value from the given string.Output should be in 
form of dict. key will be palidrome word and value will be number of occurence.
i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather
was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331. 
o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}'''


input_string = "Nittin & his mom went to a park last friday. His Mom observed that the weatherwas too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331."
input_list = input_string.split()
dict_a = {}
for i in input_list:
    if i not in  '!@#$%^&*()':
        i = i.lower()
        if i==i[::-1]:
            if i in dict_a:
                dict_a[i]+=1
            else:
                dict_a[i]=1
print(dict_a)
