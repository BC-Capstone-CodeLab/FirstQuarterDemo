'''
Farzaad Benabbas
CS 481 Senior Capstone 1 Zhiyun Li
CodeLab CodeClass

This file contains an implementation template for updating a student's grade for an assignment. Look for "MODIFY CODE HERE" in comments
to put database information when updating database.
'''
# this function takes user input for grade and then sends a string of the grade out of 100
# to the database to be stored as grade for assignment for a student
def updateAssignmentGrade():
    print("Please enter grade out of 100 for this assignment that student recieved (numerator of fraction x/100 where x is the grade).")
    try:
        inputGrade = input("Enter grade here: ")
        inputGradeNumber = float(inputGrade)
    except ValueError:
        print("Please enter a numeric value only, restarting.")
        updateAssignmentGrade()
    else:
        if inputGradeNumber < 0 or inputGradeNumber > 100:
            print("Grade must be between 0 and 100 inclusive. Please restart.")
            updateAssignmentGrade()
        else:
            grade = inputGrade + "/100"
            print(grade)
            # MODIFY CODE HERE
            #database[assignment[grade]] = grade

# testing update assignment grade function
#updateAssignmentGrade()
