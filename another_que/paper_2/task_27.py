'''27. Need to find minimum number of new chair purchase for work area with simulated set of array 
values.
C - A new employee comes to work area and new chair need to purchase
R - Employee from work area goes to meeting room and free up the chair
U - Employee comes from meeting room and occupy the chair
L - Leaves the work area and free up the chair
Input :
n = 3
simulated value : ['CCRLU', 'CRLCUC', 'CCCC']
'''

simulated_value = ['CCRLU', 'CRLCUC','CCCC']
for i in simulated_value:
    NC = 0
    CA = 0
    for j in i:   
        if j=="C" or j=="U":
            if CA>0:
                CA-=1
            else:
                NC += 1
        elif j=='R' or j=="L":
            CA+=1
    print(NC)