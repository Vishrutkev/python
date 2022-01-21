###########################################

# Name: Vishrut Kevadiya

###########################################

import random
import time
from utilities import SeaLife
from utilities import students
from utilities import studentsInfo


# import the approriate items from utilities.py and other modules may you require


def task0():
    print("Name: Vishrut Kevadiya")




def printOutcome(userSelection, computerSelection):
    if userSelection == 1:
        if computerSelection == userSelection:
            print("A tie!")
        elif computerSelection == 2:
            print("HAL Win!")
        elif computerSelection == 3:
            print("You Win!")

    elif userSelection == 2:
        if computerSelection == userSelection:
            print("A tie!")
        elif computerSelection == 3:
            print("HAL Win!")
        elif computerSelection == 1:
            print("You Win!")

    elif userSelection == 3:
        if computerSelection == userSelection:
            print("A tie!")
        elif computerSelection == 1:
            print("HAL Win!")
        elif computerSelection == 2:
            print("You Win!")


def task1():
    playagain = "y"
    while playagain == "Y" or playagain == "y":
        print("Rock, Paper, Scissors!")
        print("Make your selection. . .")
        usrinp = int(input("(1) rock, (2) paper, (3) scissors? "))
        assert usrinp > 0 and usrinp < 4, '"Invalid selection. Try again." and ask the user for input again'
        halchoice = random.randint(1, 3)
        game = {1: "rock", 2: "paper", 3: "scissor"}
        print("You: {}".format(game[usrinp]))
        print("HAL: {}".format(game[halchoice]))
        printOutcome(usrinp, halchoice)
        playagain = input("Play again (Y/N)? ")


def swapAdjacentElements(alist):
    assert len(alist) >= 2, "Must enter two or more characters!"
    for i in range(0, len(alist) - 1, 2):
        alist[i], alist[i + 1] = alist[i + 1], alist[i]
    print(alist)


def task2():
    char = input("Input two or more chars separated by spaces: ")
    print("Initial list")
    intlist = char.split()
    print(intlist)
    strver = "".join(intlist)
    print("String Version: '{}'".format(strver))
    print("Modified list")
    swapAdjacentElements(intlist)
    strver2 = "".join(intlist)
    print("String Version: '{}'".format(strver2))


def func(list, index):
    for value in list:
        if value == index:
            return True
    return False


def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    dict = {}
    for index in (range(len(students))):
        year = ""
        if func(studentsInfo["Year 1"], index):
            year = "Year 1"
        elif func(studentsInfo["Year 2"], index):
            year = "Year 2"
        elif func(studentsInfo["Year 3"], index):
            year = "Year 3"
        elif func(studentsInfo["Year 4"], index):
            year = "Year 4"

        program = ""
        if func(studentsInfo["CS"], index):
            program = "CS"
        elif func(studentsInfo["DM"], index):
            program = "DM"
        elif func(studentsInfo["BZ"], index):
            program = "BZ"
        elif func(studentsInfo["SE"], index):
            program = "SE"

        campus = ""
        if func(studentsInfo["On Campus"], index):
            campus = "On Campus"
        elif func(studentsInfo["Off Campus"], index):
            campus = "Off Campus"

        dict[students[index]] = "{:>10} ({}) Program: {} Housing: {}".format(students[index], year, program,
                                                                             campus)
    for key in sorted(dict):
        print(dict[key])
    print("\n--------- Task4: Aquarium              ------------")
    input("Press enter to start aquarium... ")
    list = []
    for i in range(5):
        list.append(SeaLife(random.randint(0, 1), random.randint(5, 30)))

    curtime = 1
    for i in range(50):

        print("{} Time : {}".format(40 * "-", curtime))
        for obj in list:
            print(obj.getStr())
            obj.move()
        time.sleep(0.3)
        curtime += 1

    input("Press enter to quit.")


if __name__ == "__main__":
    main()

