'''8. Take the input marks from user using input() function and find out the grade of the students. Note
the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the 
marks in the range 0<=marks<=100, if user will input some other marks in should print invalid 
marks.
'''

marks = int(input("Enter a marks : "))
if marks>=91:
    print("A")
elif marks <=90 and marks>=81:
    print("B") 
elif marks <= 80 and marks >=70:
    print("C")