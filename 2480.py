Dice1, Dice2, Dice3 = map(int, input().split())

if Dice1 == Dice2:
    if Dice2 == Dice3:
        reward = 10000 + (Dice1 * 1000)
        print(reward)
    elif Dice2 != Dice3:
        reward = 1000 + (Dice1 * 100)
        print(reward)

elif Dice1 != Dice2:
    if Dice1 == Dice3:
        reward = 1000 + (Dice1 * 100)
        print(reward)
    elif Dice2 == Dice3:
        reward = 1000 + (Dice2 * 100)
        print(reward)
    else:
        if Dice1 > Dice2:
            if Dice2 > Dice3 or Dice2 < Dice3:
                reward = Dice1 * 100
                print(reward)
        elif Dice1 < Dice2:
            if Dice2 > Dice3 or Dice2 < Dice3:
                reward = Dice2 * 100
                print(reward)
        elif Dice3 > Dice1:
            if Dice3 > Dice2 or Dice3 < Dice2:
                reward = Dice3 * 100