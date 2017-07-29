import random

def hangman():
    word_list = ["pennsylvania","quintessential","fart",
                 "connecticut","random","haircut","antiquated","antique"]
    random_num = random.randint(0, 4)
    word = word_list[random_num]
    wrong = 0
    # use this varibable to keep track of wrong guesses
    stages = ["",
              "__________      ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word) # a list containing each character in "word"
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        #when stages index equals zero the code
        print("\n")
        #prints a new line
        guess = input("Guess a letter: ")
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
            #if player guessed correctly the board list must b updated
            #this is done thru the index method on rletters
        elif guess == word:
            print("\n")
            print("You win! The word was {}"
                  .format(word))
            win = True
            break
        else:
            wrong += 1
            #if the guess is wrong 1 is added to the wrong
        print((" ".join(board)))
        #print the board with spaces between the letters
        e = wrong + 1
        print('\n'
              .join(stages[0: e]))
        #must use wrong plus one becuase when sliced it wont include the last index
        if "__" not in board:
            print("You win! The word was {}."
                  .format(word))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
                wrong]))
        print("\n")
        print("You lose! The word was {}."
              .format(word))


hangman()


