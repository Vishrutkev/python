####
# EECS1015 - Midterm
# Name: Vishrut Kevadiya
# Student ID: 219155290
# Email: Vishrutk@my.yorku.ca
# Section B
##

import random


def task0():
    print("""EECS1015 - Midterm
Name: Vishrut Kevadiya    
Student ID: 219155290
Email: Vishrutk@my.yorku.ca 
Section: B""")


def task1():
    name = input("Your First name: ")
    name = name.strip().capitalize()
    Lname = input("Your Last name: ")
    Lname = Lname.upper().strip()
    Ifund = float(input("Initial funds to invest: $"))
    Areturn = float(input("Annual return percentage: "))
    print("Yearly return for {} {}".format(name, Lname))
    print("Initial deposit: ${}".format(Ifund))

    for i in range(1, 6):
        Iamount = (Ifund * (Areturn / 100))
        return0 = Ifund + Iamount
        print("Year {}: ${:.2f}".format(i, return0))
        Ifund = return0
        i = 0 + 1


def task2():
    currentamt = 0
    currentamt = float(currentamt)
    print("Soda Vending Machine")
    print("Current amount ${:.2f} out of $1.00".format(currentamt))
    print("Insert Coin")

    coonie = """1. Toonie ($2.00)
2. Loonie ($1.00)
3. Quater ($0.25)
4. Dime   ($0.10)
5. Nickel ($0.05)"""
    select = 0
    while (select < 1):
        print(coonie)
        selection = input("Selection [1-5]? ")

        if (select > 1):
            print("Total amount provided: ${:.2f}".format(select))
            print("Thank you for your purchase.")
            print("Please Take Your Change ${:.2f}".format(change))

        selection = float(selection)

        selecti = coin(selection)
        if selecti == True:

            if (selection == 1):
                select += 2
            elif (selection == 2):
                select += 1
            elif (selection == 3):
                select += 0.25
            elif (selection == 4):
                select += 0.10
            elif (selection == 5):
                select += 0.05
            elif selecti == False:
                print("Invalid Selection!")

        if (select >= 1):
            break

        print("Current amount ${:.2f} out of $1.00".format(select))
        print("Insert Coin")
    change = select - 1

    if (select == 1):
        print("Total amount provided: ${:.2f}".format(select))
        print("Thank You for your purchase.")
    else:
        print("Total amount provided: ${:.2f}".format(select))
        print("Thank you for your purchase.")
        print("Please Take Your Change ${:.2f}".format(change))


def coin(selection):
    select = 0
    if (selection > 0) and (selection < 6):
        return True
    else:
        print("Invalid Selection!")
        return False


def task3():
    num = 0
    count = 0
    sum = 0
    i = 1
    print("Dice Game")
    print("Rolling Die 10 Times")
    for i in range(1, 11):

        dice = random.randint(1, 6)
        print("Roll {}: [{}]".format(i, dice))
        num += dice
        i = i + 1
        if (dice == 1):
            count = count + 1
    if (count == 2):
        bonus = 10
        num += 10
        print("+10 Bonus for snake eyes [1][1]!")

    if (num > 35):
        print("Total {} -- OVER 35 POINTS [YOU WIN!]".format(num))
    elif (num <= 35):
        print("Total {} -- TOO FEW POINTS [YOU LOSE!]".format(num))

    again = input("Enter 'Y' to play again: ")
    if (again == 'Y' or again == 'y'):
        task3()


def countCases(string):
    i = 0
    sum = 0
    sum0 = 0

    for i in range(0, len(string)):

        if string[i] >= "A" and string[i] <= "Z":
            upr = str((len(string[i])))
            if upr == "1":
                upr = int(upr)
                sum += upr
        else:
            if string[i] >= "a" and string[i] <= "z":
                upr1 = str((len(string[i])))
                if upr1 == "1":
                    upr1 = int(upr1)
                    sum0 += upr1

    return sum, sum0


def flipCase(string):
    string = string.swapcase()
    return string


def cutQuotedText(string):
    sum = 0

    start = -1
    end = -1

    ind = 0

    for i in string:

        if (i == '"' and start == -1):
            start = ind
        elif (i == '"' and end == -1):
            end = ind + 1
            sum = 1

        elif (i == '"'):
            sum = 0
        ind += 1

    if (sum == 1):
        String = string[start: end]
        string = string.replace(String, '')
        return "'" + string + "'"

    return "'ERROR! No quoted text'"


# main function for EECS1015 midterm
def main():
    print("\n")
    task0()

    print("\n----------Task 1-----------")
    task1()

    print("\n----------Task 2-----------")
    task2()

    print("\n----------Task 3-----------")
    task3()

    print("\n----------Task 4-----------")
    string = input("Enter string with one word with \"quotes\": ")
    sum, sum0 = countCases(string)
    print("This String has {} Upper Case Characters.".format(sum))
    print("This String has {} Lower Case Characters.".format(sum0))
    print("Case flip: \'{}\'".format(flipCase(string)))
    print("Quote removed: {}".format(cutQuotedText(string)))

    input("\nPress enter to exit.")


if __name__ == "__main__":
    main()
