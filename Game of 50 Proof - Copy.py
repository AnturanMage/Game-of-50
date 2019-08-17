import random
one = 0
two = 0


def init():                           #This is the topmost level of the program. It initializes the program, takes user input to define Player One's strategy and the number of games to be played.
    global one
    global two
    global Round
    global strat
    one = 0
    two = 0
    strat = int(input('What strategy should Player 1 use? \nInput 0 for a random strategy and input 1 for the winning strategy. \nPlayer 2 always chooses random numbers.\n'))
    times = int(input('How many games shall be played?\n'))
    Round = 1
    for x in range(times):            #This is the main game loop
        game()
        Round += 1
    print('The games of 50 are over. Player 1 won %d times, and Player 2 won %d times.' % (one, two))
    redo = input('Play again? (y/n)\n')
    if redo == 'y':
        init()
    elif redo == 'n':
        print('Goodbye')
    else:
        print("I don't understand. Please input only y or n.")


def game():                           #This is the function that defines the behavior of the game of 50.
    global Round
    global one
    global two
    subtotal = 0
    numlist = []
    print('Game %d' % Round)
    print('Player 1   Player 2   TOTAL')
    while True:
        playeronemove(strat, numlist) #Player one moves
        subtotal += numlist[-1]
        if subtotal>= 50:             #Is the game over?
            one += 1
            print('%d          -          %d' % (numlist[-1], subtotal))
            print('Player 1 Wins\n\n')
            break
        playertwomove(numlist)        #Player two moves
        subtotal += numlist[-1]
        if subtotal >= 50:            #Is the game over?
            two += 1
            print('%d          %d          %d' % (numlist[-2], numlist[-1], subtotal))
            print('Player 2 Wins\n\n')
            break
        print('%d          %s          %d' % (numlist[-2], numlist[-1], subtotal))


def playeronemove(strat, numlist):    #Defines Player one's behavior. Player one is programmed with multiple strategies, thus its function is slightly longer.
    if strat:
        if not numlist:
            numlist.append(1)
        else:
            numlist.append(random.randint(1, 6))
    else:
        numlist.append(random.randint(1, 6))


def playertwomove(numlist):           #Defines Player Two's behavior.
    numlist.append(random.randint(1, 6))

init()
