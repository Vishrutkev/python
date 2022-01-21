###################
#
# Lab 9
# *****IMPORTANT*****
# ADD YOUR INFO HERE REQUIRE BY TASK 0
# Lab 9
# Author: Vishrut Kevadiya
# Email: vishrutk@my.yorku.ca
# Student ID: 219155290
# Section: B
# IMPLEMENT MinMaxList.py
# UPLOAD BOTH FILES USING WEBSUBMIT
# ->>>>DO NOT ZIP/RAR<<<<<--- YOUR FILES  (50% off if you zip)
#
###################

from MinMaxList import MinMaxList
from random import randint

# Main function is given.
def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])

    print("Insert Item")
    for i in range(30):
        x = randint(1, 100)
        aList.insertItem(x, True)

    print("---Get Min---")
    for i in range(10):
        print("Min item %d " % aList.getMin())
        aList.printList()

    print("---Get Max---")
    for i in range(10):
        print("Max item %d " % aList.getMax())
        aList.printList()

if __name__ == "__main__":
    main()
