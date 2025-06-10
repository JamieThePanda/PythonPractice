print("Challenge 4")
print("Finding consonants")
list = [2,4,3,5,6,7,2]
consanants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")#Tuple for consonants
vowels = ("a","e","i","o","u") #Tuple for vowels

word = str(input("Please enter your word: "))

def consanants(word): #define consanants(word) cycle list through word
    word = word.lower() #Puts word into lower case to define
    countc = 0 #countc variable = 0
    for char in word: #For character in word
        if char in "bcdfghjklmnpqrstvwxyz": #If character IS in consanants list
            countc +=1 #countc variable increases by 1
    return countc #Return final count of consanants
     
print("You have", consanants(word), "consonants in word:", word)

