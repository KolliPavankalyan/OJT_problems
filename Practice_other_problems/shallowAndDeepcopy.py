#shallowCopy 
import copy
list1 = [[1,2,3,4],[5,9,5,8]]
list2 = list1.copy()
list2[0][0]=10
print(list1,list2)


#DeepCopy
li1 = [[1,2,3,4],[5,9,5,8]]
li2 = copy.deepcopy(li1)
li2[0][0] = 10
print(li1,li2)


#shallowCopy 
import copy
list1 = [1,2,3,4]
list2 = list1.copy()
list2[0]=10
print(id(list1), id(list2))
print(list1,list2)


#DeepCopy
li1 = [1,2,3,4]
li2 = copy.deepcopy(li1)
li2[0] = 10
print(li1,li2)


