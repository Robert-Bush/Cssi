score = 0

draw = "yes"
while (draw == "yes"):




    draw = raw_input("Would you like to draw a card")

    if (draw == "yes" or score > 21):

        import random
        for x in range(1):
            card = random.randint(2,12)
        if  card == 1 or card == 11:
            list = [1,11]
            card = random.choice(list)
        pass
        score = card + score
        print("you drew a ", card)
        print("your score is", score, )

        if score >= 21:
            break
            pass
    else:
        break




        pass
        pass

if score:
    pass

print("you're final score was ", score)
