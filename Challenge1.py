print("Challenge 1") #Intro message

user_input = int(input("Enter a number:")) #Asks user to input integer value

if user_input >0: #If the user enters a number greater than 0
                 print("Number is a positive") #Passes condition, is positive

                 if user_input %2 == 0: #Checks if the number is even
                     print("It is even") #If passes above condition, prints
                 else: #Otherwise it is not even
                     print("It is odd") #If passes above condition, prints



elif user_input == 0: #If user enters zero
    print("Your number is 0") #If above passes condition, prints

else: #Else, if no other conditon is passed
    user_input <=0 #This is what occurs, a negative ineger is inputted
    print("Number is a negative") #if passes above conditon, prints

