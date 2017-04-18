# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    
    for s1 in secretWord:
        letterIsIn=False
        for s2 in lettersGuessed:
            if s1==s2:
                letterIsIn=True
        if letterIsIn==False:
            return False
    return True
                
                
    
    # FILL IN YOUR CODE HERE...



def isLetterGuessed(lettersGuessed,letter):
    
    for s1 in lettersGuessed:
        if letter==s1:
            return True

    return False

def letterInWord(word,let):
    for s in word:
        if s==let:
            return True
    return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord=""
    i=0
    for s1 in secretWord:
        letterIsIn=False
        for s2 in lettersGuessed:
            if s1==s2:
                letterIsIn=True
        if letterIsIn==False:
            guessedWord=guessedWord+"_ "
        else:
            guessedWord=guessedWord+s1
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters="abcdefghijklmnopqrstuvqxyz"
    availableLetters=""
    i=0
    for s1 in letters:
        letterIsIn=False
        for s2 in lettersGuessed:
            if s1==s2:
                letterIsIn=True
        if letterIsIn:
            availableLetters=availableLetters+""
        else:
            availableLetters=availableLetters+letters[i]
        i=i+1
    return availableLetters
    

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
    guesses=12
    lettersGuessed=""
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("-------------")
    
    while guesses>0:
        print("You have "+str(guesses)+" guesses left.")
        print("Available letters: "+getAvailableLetters(lettersGuessed))
        newLetter=input("Please guess a letter: ")
        if isLetterGuessed(lettersGuessed,newLetter):
            print("Oops! You've already guessed that letter")
            guesses=guesses+1
        else:
            lettersGuessed=lettersGuessed+newLetter
            if letterInWord(secretWord,newLetter):
                print("Good Guess: "+getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
        print("--------------")
        if isWordGuessed(secretWord, lettersGuessed):
            return "Congratulations, you won!"
            guesses=0
            
            
        
        
        
        guesses=guesses-1
    
    return ("Sorry, you ran out of guesses. The word was "+secretWord)

    


print(hangman(chooseWord(wordlist)))




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)