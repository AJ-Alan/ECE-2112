#Alphabet Soup Problem#
#Create a function that takes a string and returns a string with its letters in alphabetical order

def alphabet_soup(s): #define function "alphabet_soup" that sorts the letters of input string where the input is the variable s
    s = list(s) #converts s into a list
    s.sort() #sorts the list in alphabetical order
    print("".join(s)) #prints the function that converts the list back into a string
    
#starts main function
s = str(input("\nEmoticon converter\nEnter a word:")) #sets the variable s as a string input
alphabet_soup(s) #calls function "alphabet_soup"


#Emoticon Problem#
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


#Unpacking List Problem#
#Create a function that unpacks the list [write your code here] into three variables: first, middle, and last
#where the first and last are the respective first and last values of the list and the middle is everything else in between
#Then print all three variables

def unpack(s): #define function "unpack" which will create 3 variables from input s and prints them out
    first = s[0] #sets the "first" variable to be equal to the first element of the list
    last = s[len(s)-1] #sets the "last" variable to be equal to the last element of the list
    s.remove(s[0]) #removes the first element
    s.remove(s[len(s)-1]) #removes the last element
    middle = s #sets the "middle" variable to be the rest of the elements of the list
    print("first: ",first,"\tmiddle: ",middle,"\tlast: ", last) #prints out the elements of the list

#starts main function
s = input("Please input a list and separate it with commas: ") #sets the input string to s
s = s.split(",") #splits s into a list with "," as the separator
unpack(s) #calls function unpack with input s
