# firstName = raw_input("first name?")
# lastName = raw_input("last name?")
#
# print(firstName + " " + lastName)
#
# print("Hello World!")
#
# print("Lil" + firstName + "the" + lastName)
i = 0
scoreOne = 0
scoreTwo = 0

rounds = input("Amount of rounds you want to play")
while  (i < rounds):



    playerOne = raw_input("Enter r, p, or s")
    playerTwo = raw_input("Enter r, p, or s")
    i = i + 1


    if (playerOne == playerTwo):
        print("Tie")
    elif (playerOne == "r" and playerTwo == "s" or playerOne == "s" and playerTwo == "p" or playerOne == "p" and playerTwo == "r"):
        print("player one wins")
        scoreOne = scoreOne + 1
    else:
        print("player two wins")
        scoreTwo = scoreTwo + 1

    print("Player 1 is"  ,scoreOne, "Player 2 is " ,scoreTwo,)


    pass

if  (scoreOne > scoreTwo):
    print("Player 1 is the Winner!")
elif (scoreOne == scoreTwo):
    print("It's a Tie!!")
else:
    print("Player 2 is the Winner")
    pass

    
