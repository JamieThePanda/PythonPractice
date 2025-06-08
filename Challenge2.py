print("Challenge 2") # Intro message

print("This is the grade sorting automatic") #Intro message

user_grade = int(input("Please enter a number between 1-100: ")) #Asking for user input



if user_grade >= 90 and user_grade <=100: #Condition, input is equal or greater than 90 but less than or equal to 100
    print("Grade A")                      #If above condition pass - print

elif user_grade >=80 and user_grade <=89: #Condition input is between 80-89
    print("Grade B")                      #If above condition pass - print

elif user_grade >=70 and user_grade <=79: #Condition input is between 70-79
    print("Grade C")                      #If above condition pass - print

elif user_grade >=60 and user_grade <=69: #Condition input is between 60-69
    print("Grade D")                      #If above condition pass - Print

elif user_grade <=60 and user_grade >=0: #User input is less than 60 but greater than or equal to 0
    print("Grade F")  #If above condition pass - print
     

else: #Else if none of the above conditions are passed
    user_grade >=101 or user_grade <0 #Int input user_grade has inputted number greater than 100 or less than 0
    print("Invalid score. Please enter a number between 0 and 100.") #Out of range friendly error message with new simple instruction
    user_grade = int(input("Please enter a number between 1-100: ")) #Give them a loop / chance to re-enter a new value
