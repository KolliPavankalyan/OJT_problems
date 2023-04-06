'''20. Write a python program for sort the given below list based last character of each word
names_list = ['Prabhu', Rahul', 'Arunesh, 'Sonali', 'Rakshit']'''


#Approach2
name_list = ["Prabhu","Rahuu","Arunesh","Sonali","Rakshit"]
print(sorted( name_listkey=lambda x: x[-1]))



#Approach 2:
name_list1 = [i[::-1]for i in name_list]
name_list1.sort()
print([ i[::-1] for i in name_list1])