#Writing a program to find out how many times a given character is given in a word using nested loop with the outer loop being a while loop and the inner loop being a for loop.

word=input("Enter a word:")
character=input("Enter a character to find out how many times it is repeated in the word:")

i=0
count=0

while i<len(word):
    if word[i]==character:
            count+=1
    i+=1
   
print("The character",character,"is repeated",count,"times in the word",word)