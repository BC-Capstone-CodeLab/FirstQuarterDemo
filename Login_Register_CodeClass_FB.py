'''
Farzaad Benabbas
CS 481 Senior Capstone 1 Zhiyun Li
CodeLab CodeClass 

This file contains implementation template of registration and login functions for the CodeClass website.
Please modify template with corresponding database information to make use of functions correctly. Look for
"MODIFY CODE HERE" in comments.
Video link used as tutorial: https://www.youtube.com/watch?v=dR_cDapPWyY
'''

# function allows user to register to CodeClass using a username not already in database and any password
def register():
    # establish connection to database
    database = open("database.txt", "r")
    userName = input("Create username: ")
    password0 = input("Create password: ")
    password1 = input("Confirm password: ")
    # checking for user input
    if len(userName) < 1 or len(password0) < 1 or len(password1) < 1:
        print("Username or password must be 1 or more characters. Please try again.")
        register()
    # check to see if passwords match when verifying password when creating account
    elif password0 != password1:
        print("Passwords do not match, please restart.")
        register()
    # check to see if username already taken in database
    # MODIFY CODE HERE
    elif userName in database:
        print("Username already taken, please restart.")
        register()
    # add user to database
    # MODIFY CODE HERE
    else:
        database = open("database.txt", "a")
        database.write(userName + ", " + password0 + "\n")
        print("Account created successfully.")

# testing register function
#register()

# function allows user to login to CodeClass with an account that already exists in database
def login():
    # establish connection to database
    database = open("database.txt", "r")
    userName = input("Enter username: ")
    password = input("Enter password: ")
    # checking for user input
    if len(userName) < 1 or len(password) < 1:
        print("Username or password must be 1 or more characters. Please try again.")
        login()
    # if username exists and password matches with password associated with that username then 
    # login is successful and user can access website with the account
    # MODIFY CODE HERE
    elif userName == database[userName] and password == database[password]:
        print("Login successful.")
    else:
        print("Invalid username or password. Please try again.")
        login()

# testing login function
#login()






