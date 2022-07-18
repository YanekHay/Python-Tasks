## Exercise 157: Both Letter Grades and Grade Points
letterGrades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
numGrades =    [4   ,3.9,3.7 ,3.3 ,3  ,2.7 ,2.3 ,2  ,1.7 ,1.3 ,1  ,0.7 , 0]

##This line is a comment
while True:
    grade = input("Enter a grade >>> ")
    if grade == "":
        break
    else:
        #This is a comment too
        try:
            grade = float(grade)
        except:
            if grade in letterGrades:
                print(f"Your numeric grade is {numGrades[letterGrades.index(grade)]}")
            else:
                print("Wrong grade is entered!")
        else:
            # Again a comment
            if numGrades[-1]<=grade and grade<=numGrades[0]:
                for i in range(1,len(numGrades)):
                    if numGrades[i]<=grade and numGrades[i-1]>=grade:
                        print(f"Your grade with letter is {letterGrades[i]}")
                        break
            else:
                print("Wrong grade is entered!")