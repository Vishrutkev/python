################
# Lab 4
# Author: Vishrut Kevadiya
# Email: vishrutk@my.yorku.ca 
# Student ID: 219155290
# Section B
###############


# you'll need the random module
import random

### Write your functions below ###
spoints = 100
cpoints = spoints
Game = True
crounds = 1
mrounds = 10
print("\n")
tCards = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "T", 11: "J", 12: "Q", 13: "K",
          14: "A"}


def vCards():
    return random.randint(2, 14)


def sCards(vCards):
    return tCards[vCards]


def guesshighlow():
    guess = ""
    while guess not in ["H", "L", "h", "l"]:
        guess = input("High or Low (H/L)?: ")
    if guess in ["H", "h"]:
        return "HIGH"
    elif guess in ["L", "l"]:
        return "LOW"


def betamount(maxamount):
    bettingAmount = 0
    while bettingAmount < 1 or bettingAmount > maxamount:
        bettingAmount = int(input("Input bet amount: "))
    return bettingAmount


def Guessing(dice1, dice2, Type):
    if (dice1 > dice2 and Type == "LOW") or ((dice1 < dice2 and Type == "HIGH")):
        return True
    else:
        return False


def function(points, rounds, status):
    print("----------------{}-----------------".format(status))
    print("YOU MADE IT TO *{}* POINTS IN {} ROUNDS!".format(points, rounds))
    print("-----------------------------------")


### Write your main program below ####
msg = """--- Welcome to High-Low ---
Start with 100 points.  Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose. 
Try to make it to 500 points within 10 tries."""

print(msg)
while Game:
    print("--------------------------------------------")
    print("OVERALL POINTS: {} ROUND {}/{}".format(cpoints, crounds, mrounds))
    card_1 = vCards()
    Card1 = sCards(card_1)
    print("First card is a [{}]".format(Card1))
    guessing = guesshighlow()
    bettingamount = betamount(cpoints)
    card_2 = vCards()
    Card2 = sCards(card_2)
    result = ""
    Correct = Guessing(card_1, card_2, guessing)
    result = ""
    if Correct == True:
        cpoints += bettingamount
        result = "WON"
    else:
        cpoints -= bettingamount
        result = "LOST"
    print("Second card is a [{}]".format(Card2))
    print("Card1 [{}] Card 2 [{}] - You bet '{}' for {} - YOU {}".format(Card1, Card2, guessing, bettingamount, result))
    if cpoints >= 500:
        function(cpoints, crounds, "WIN")
        break
    elif cpoints <= 0 or crounds == mrounds:
        function(cpoints, crounds, "LOSE")
        break
    else:
        crounds += 1

input("Press enter to exit. ")  # input statement to pause code when finished