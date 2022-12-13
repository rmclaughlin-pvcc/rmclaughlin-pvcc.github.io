# Name: Ryan McLaughlin
# Program Purpose: Pordle (PVCC Wordle): Word Guessing Game
#   The program chooses a random word from a file of words. The user tries to 
#   figure out the word in the fewest guesses by guessing letters in the word.
#   This program uses an input FILE, LISTS and STRING SLICES (section of the string)

import random
wordList = []
inFile = "animals.txt", "food.txt", "cars.txt", "sports.txt"
global wordFile

def main():
    global wordList, inFile 
    playAgain = True
    while playAgain:
        printHeadings()
        printMenu()

        wordFile = open(inFile, "r")  #open this file for read
        for textLine in wordFile:     #read in a line of text from the file
            for word in textLine.split():  #split the line of text into words
                wordList.append(word)   #add each word to the word list
        wordFile.close()

        playGame()
        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == "n" or yesno == "N":
            playAgain = False;
            print("Thank you for playing PORDLE!")
            return()

def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")
    
def printMenu():
    global inFile
    print("\nChoose a PORDLE category:")
    print("\t1. Animals")
    print("\t2. Foods")
    print("\t3. Cars")
    print("\t4. Sports")
    category = input("Please enter a category number: ")

    if category == "1":
        inFile = 'animals.txt'
    elif category == "2":
        inFile = 'foods.txt'
    elif category == "3":
        inFile = 'cars.txt'
    elif category == "4":
        inFile = 'sports.txt'
    else:
         inFile = 'animals.txt'
         print("This will be an ANIMAL Pordle (next time please select a number 1-4)")     #Else for the category incase another number is typed instead of an error popping up 


def playGame():
    numguesses = 1
    lettersUsed = []

    wordChosen = random.choice(wordList)
    pordle = wordChosen
    for i in range (len(pordle)):
        pordle = pordle[0:i] + "_" + pordle[i+1:]     #Use SLICE to replace each letter with a '_'
    print(" ".join(pordle))         #the "join" will put a space between each underscore

    while pordle != wordChosen:     #keep asking the player until player guesses the word
        letterGuess = input("Please enter a letter: ")
        letterGuess = letterGuess.lower()
        lettersUsed.append(letterGuess)    #Add the players' letter to the list of huessed letters
        print ("Number of guesses: " + str(numguesses))

        for i in range(len(wordChosen)):    #search through the letters to find a match 
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]
            
        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle))       #print the string with guessed letters with spaces in between
        numguesses += 1

    print("Well done! You guessed in " + str(numguesses-1) + " guesses!")

main()