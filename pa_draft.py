#Create a function that takes a string and returns a string with its letters in alphabetical order

def alphabet_soup(s): #define function "alphabet_soup" that sorts the letters of input string where the input is the variable s
    s = list(s) #converts s into a list
    s.sort() #sorts the list in alphabetical order
    print("".join(s)) #prints the function that converts the list back into a string
    
#starts main function
s = str(input("\nEmoticon converter\nEnter a word:")) #sets the variable s as a string input
alphabet_soup(s) #calls function "alphabet_soup"

#Create a function that changes specific words into emoticons
#Smile -> :) , Grin -> :D , Sad -> :(( , Mad -> >:(, lmao -> XD ##added lmao for me XD

def emotify(s): #define function "emotify" that will find specific strings to change them into emoticons
    s = s.split() #splits words in s into a list and re-equating to s
    for x in s: #begins for loop to each specific words 
        chaEmo(s,"smile",":)") #the following calls function chaEmo with inputs s, specific word, respective emoticon
        chaEmo(s,"grin",":D")
        chaEmo(s,"sad",":((")
        chaEmo(s,"mad",">:(")
        chaEmo(s,"lmao","XD")
    s = " ".join(s) #converts the list back into a string with spaces in between the words
    print("\n",s) #prints 

def chaEmo(s,word,emoticon): #generalized function that changes the values
    try: #tries the following function and excepts an error if it occurs
        il = s.index(word) #set il as the index with word from s
        s.remove(word) #remove word from s
        s.insert(il,emoticon)  #insert [corresponding emoticon] to s on index il
        return s #returns the value to s
    except: #there's an error where the statements above tries to find a non-existent value, this try-except statement will cancel that error from happening 
        pass

#starts main function
s = str(input("Enter a sentence: ")) #sets the input string to s
emotify(s) #calls function emotify with input s
