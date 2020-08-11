import random, time
fruit_list= ['guava', 'mango', 'apple', 'banana', 'orange', 'pineapple','cantaloupe', 'grapes','pear','dates']
guesslist = []
userguesses = []
PlayAgain = True
continueGame = "Y"
name = input("Enter your name ")
print("Hello", name.capitalize(), "let's play Hangman!")
time.sleep(0.5)

while True:

    secretWord = random.choice(fruit_list)
    secretWordList = list(secretWord)
    attempts = (len(secretWord) + 2)


    def printGuessedLetter():
        print("Your Secret word is: " + ''.join(guesslist))


    for n in secretWordList:
        guesslist.append('_')
    printGuessedLetter()

    print("The number of allowed guesses for this word is:", attempts)

    while True:

        print("Guess a letter:")
        letter = input()

        attempts -= 1
        userguesses.append(letter)
        if letter in secretWordList:
            print("Nice guess!")
            if attempts > 0:
                print("You have ", attempts, 'guess left!')
            for i in range(len(secretWordList)):
                if letter == secretWordList[i]:
                    letterIndex = i
                    guesslist[letterIndex] = letter.upper()
            printGuessedLetter()

        else:
            print("Oops! Try again.")
            if attempts > 0:
                print("You have ", attempts, 'guess left!')
            printGuessedLetter()

        joinedList = ''.join(guesslist)
        if joinedList.upper() == secretWord.upper():
            print("Yay! you won.")
            break
        elif attempts == 0:
            print("Too many Guesses!, Sorry better luck next time.")
            print("The secret word was: " + secretWord.upper())
            break

    continueGame = input("Do you want to play again? Y to continue, any other key to quit ")
    if continueGame.upper() == 'Y':
        guesslist = []
        userguesses = []
        PlayAgain = True
    else:
        exit("Thank You for playing. See you next time!")
