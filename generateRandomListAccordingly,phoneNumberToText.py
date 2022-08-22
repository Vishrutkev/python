#########################
# EECS1015 - Lab 5
# name : Vishrut Kevadiya
# student ID : 219155290
# email : vishrutk@my.yorku.ca
# Section : B
#########################

import random


# Task1 function

def main():
    def generateRandomList(listsize, maximumintegervalue):

        while listsize >= 0:

            randomlist = []
            avg = 0
            for i in range(listsize):
                maxint = random.randint(0, maximumintegervalue)
                maxint = int(maxint)
                avg += maxint
                randomlist.append(maxint)
            return randomlist

    def computeAverage(value):
        avg = float(sum(value)) / len(value)
        return avg

    # Task2 function

    def stringToCharLst(string):
        lenstring = []
        for i in string:
            lenstring.append(i)
        return lenstring

    def charsToWord(string):
        dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                '8': 'eight', '9': 'nine', '-': 'dash'}
        dictword = []
        for i in string:
            dictword.append(dict[i])
        return dictword

    print("\n--------- TASK 1: Random List -------------")

    listsize = int(input("Input list size: "))
    maximumintegervalue = int(input("Input max int: "))
    value = generateRandomList(listsize, maximumintegervalue)
    print("Generated list")
    print(value)

    avg = computeAverage(value)
    print("Average Value = {:.4f}".format(avg))

    print("\n--------- TASK 2: Phone number to text ---")

    print("Enter phone number as XXX-XXX-XXXX")
    string = input("Type here: ")
    str = stringToCharLst(string)
    print(str)

    dictwords = charsToWord(string)
    print(dictwords)

    separator = "->"
    z = separator.join(dictwords)
    print(z)

    input("Press enter to exit.")


if __name__ == "__main__":
    main()