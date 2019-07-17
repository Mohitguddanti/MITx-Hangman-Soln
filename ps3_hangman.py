# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ""
    for x in secretWord:
        if x in lettersGuessed:
            guess = guess + x
        else:
            guess = guess + "_ "
    return guess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    getAvail = string.ascii_lowercase
    for x in lettersGuessed:
	    if x in getAvail:
		    getAvail = getAvail.replace(x,"")
    return getAvail

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to Hangman !\nI'm thinking of a word with "+str(len(secretWord))+" letters.")
    chance = 8
    
    lettersGuessed = []
    while chance > 0:
        if isWordGuessed(secretWord,lettersGuessed):
            print("You've Won ! Thats the word i thought of ! Yay!")
            break
        print("-------------------------------------------\n")
        print("You have " + str(chance) + " guesses left.\n")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        x = input("Please guess a Letter : ")
        if x in lettersGuessed and x not in getAvailableLetters(lettersGuessed):
            print("Oops! you've already guessed that letter ! " + getGuessedWord(secretWord,lettersGuessed)+ "\n")
            print("-------------------------------------------\n")
            chance = chance + 1
        lettersGuessed.append(x)    
        if x in secretWord:
            print("Good guess: " + getGuessedWord(secretWord,lettersGuessed)+ "\n")
            print("-------------------------------------------\n")
        else:
            print("Oops ! That letter is not in my word.\n")
            print("-------------------------------------------\n")
            chance = chance - 1
                
    if chance == 0:
        print("You've been hanged xD")
        print(secretWord)
    y = input("Try Again ? (Y/N) :")
    if y == 'Y':
        secretWord = chooseWord(wordlist).lower()
        hangman(secretWord)
    else:
        return 0
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
