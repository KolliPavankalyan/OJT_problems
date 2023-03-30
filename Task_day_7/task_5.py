'''5. Let's consider there is a list which contains usernames, You have received requirement to add one more username to the list (without using append and assignment approaches) 
input : ["user1","user2"] 
output: ["user1","user2","user3"]'''

def add_item(li,item):
    return li+[item]
li_items = input("Enter the list of users  :").split()
item = input("Enter added item  :")
print(add_item(li_items,item))
