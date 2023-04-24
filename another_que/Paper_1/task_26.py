'''You are given a string S. Your task is to find the indices of the start and end of string k in
S
The first line contains the string S.The second line contains the string k.
Print the tuple in this format: (start _index, end _index). If no match is found, print (-1,
-1).
'''

a = "aaabbbssjsskaaaa"
b = "aa"
for i in range(0,len(a),1):
    if b==a[i:len(b)+i]:
        print((i,len(b)+i-1))
        