print("Welcome to challenge 3") #Intro message
even = 0 #Assigning even with a base value
odd = 0 #Assigning odd with a base value

for nums in range(1,6): #Made a simple range loops 5 times, set index 6 because it is excluded. Easier as there is a set number of inputs a user has. Originally put just (range 5) but looks messy as first value prints 0. 
    val = int(input("Enter a number: ")) #Assigning the variable of the inputted value
    #nums+=1 Variable will add 1 each time, so it will reach 5(I removed this, I realised this was something I did in the past and it looks messy and was unecessary, removed it and updated the range function instead.)
    print(nums, "Value has been assigned a value of", val)

    if val %2 == 0: #If val is %2 it is even, so even variable will add one. 
              even+=1

    else: #Else if it not %2 it must be an odd number, so odd variable will add one. 
        odd+=1


#I did originally put Else: in there but not really necessarily, it COULD be added to improve readability, to show it is attached to the same sort of function here, but ALAS, it is the only thing we are doing, so it looks neater. 
print("You have successfully inputted 5 numbers") #Simple, thanks for being good and doing as instructed. 
print("You have",even,"even numbers and",odd,"odd numbers.")#Final output that shows, you have inputted x amount of even and x amount of odd. 

