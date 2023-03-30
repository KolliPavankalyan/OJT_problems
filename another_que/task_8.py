'''8. Take the input marks from user using input() function and find out the grade of the students. Note
the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the
marks in the range 0<=marks<=100, if user will input some other marks in should print invalid
marks.'''

given_marks = int(input("Enter the the marks  :"))
if given_marks>=91:
    print("A1")
elif given_marks<=90 and given_marks>=81:
    print("A2")
elif given_marks<=80 and given_marks>=71:
    print("B1")
elif given_marks<=70 and given_marks >= 61:
    print("B2")
elif given_marks<=60 and given_marks>=51:
    print("C1")
elif given_marks<=90 and given_marks>=81:
    print("C2")
else:
    print("Fail")


#Approch 2:

