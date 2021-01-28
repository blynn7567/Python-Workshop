import time
import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
fiveLetterWordList = list()
correctGuesses = list()
wrongGuesses = list()

def main():
    for word in WORDS:
        if len(word) == 5:
            fiveLetterWordList.append(word.decode('utf-8'))

    name = input("Hi there. Do you want to play Hangman with me? Y/N: ")

    if name in "Y":
        print("I'll pick a five-letter word...")
        word = random.choice(fiveLetterWordList)
        time.sleep(1)

        guesses = input("Guess a letter: ")
        turns = 10

        while turns > 0:
            fails = 0
            word2 = ""
            for char in word:
                if char in guesses:
                    word2 = word2 + char + " "
                    # print("Your correct letters are: " + char)
                else:
                    word2 = word2 + "_ "
                    # print("oops, that's not right.")
                    fails += 1
            print("Word so far: " + word2)
            if fails == 0:
                print("Yay, you win!")
                print("= ^ - _ - ^ =")
                break
            print("You have tried: " + guesses)
            #ask for a guess
            guess = input("Guess a letter: ")
            guesses = guesses + " " + guess

            if guess not in word:
                turns -= 1
                # print "Wrong"
                print("No pressure, you have " + str(turns) + " more guesses.")
                responses = printMan(turns)
                # man = man + responses
                print(responses)
                if turns == 0:
                    print("Oops, you lost. The secret word was " + word)

    else:
        print("I didn't want to play with you anyway.")

def printMan(turns):
    if turns is 10:
        print("10 yo")
    if turns is 9:
        return "|-------\n" \
               "|      O\n" \
               "|      \n"
    if turns is 8:
        return "|-------\n" \
               "|      O\n"\
               "|      |\n" \
               "|      \n"
    if turns is 7:
        return "|-------\n" \
               "|      O\n" \
               "|      |\n"\
               "|     /\n" \
               "|      \n"
    if turns is 6:
        return "|-------\n" \
               "|      O\n" \
               "|      |\n" \
               "|     / \\ \n" \
               "|      \n"
    if turns is 5:
        return "|-------\n" \
               "|      O\n" \
               "|      |\n" \
               "|     / \\ \n"\
               "|    /\n" \
               "|      \n"
    if turns is 4:
        return "|-------\n" \
               "|      O\n" \
               "|      |\n" \
               "|     / \\ \n" \
               "|    /   \\\n" \
               "|      \n"
    if turns is 3:
        return "|-------\n" \
               "|      O\n" \
               "|     -|\n" \
               "|     / \\ \n" \
               "|    /   \\\n" \
               "|      \n"
    if turns is 2:
        return "|-------\n" \
               "|      O\n" \
               "|     -|-\n" \
               "|     / \\ \n" \
               "|    /   \\\n" \
               "|      \n"
    if turns is 1:
        return "|-------\n" \
               "|      O\n" \
               "|    --|-\n" \
               "|     / \\ \n" \
               "|    /   \\\n" \
               "|      \n"
    if turns is 0:
        return "|-------\n" \
               "|      O\n" \
               "|    --|--\n" \
               "|     / \\ \n" \
               "|    /   \\\n" \
               "|      \n"

if __name__ == "__main__":
    main()
