#########################
# EECS1015 - York University
# Lab #7 - Starting Code
#  Writing test cases
#  Make sure you install PyTest (see lecture notes)
#  NOTE - You can only run this in PyCharm for a project that has installed PyTest
#  You cannot double click on this file.  That is fine, we can test it once you submit it.
#########################

# Lab 7 #
# Author: Vishrut Kevadiya
# Email: vishrutk@my.yorku.ca
# Student ID: 219155290
# Section: B

import pytest
from typing import List

# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()

def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    assert minormax.upper()=="MAX" or minormax.upper()=="MIN", "2nd argument must be 'Min' or 'Max' "
    length = len(myList)
    assert length != 0, "Error: List is empty"
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result

# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE
# Lab 7 #
# Author: Vishrut Kevadiya
# Email: vishrutk@my.yorku.ca
# Student ID: 219155290
# Section: B
######

def  test_getMinMaxCase1():
    List1 = [12,25]
    initializeMinMaxList(List1)
    mini = getMinMax(List1, "MIN")
    assert mini == 12, "Min should be 12"
    maxi = getMinMax(List1, "MAX")
    assert maxi == 25, "Min should be 25"

def  test_getMinMaxCase2():
    List2 = [10]
    initializeMinMaxList(List2)
    min = getMinMax(List2, "MIN")
    assert min == 10,"Min should be 10"
    insertItem(List2, min)
    max = getMinMax(List2, "MAX")
    assert max == 10, "Max should be 10"

def  test_getMinMaxCase3():
    List3 = []
    initializeMinMaxList(List3)
    insertItem(List3, 5)
    insertItem(List3, 55)
    min = getMinMax(List3, "MIN")
    assert min == 5, "Min should be 5"
    max = getMinMax(List3, "MAX")
    assert max == 55, "Min should be 55"

def  test_getMinMaxRequestError():
    List4 = [1,23,15]
    initializeMinMaxList(List4)

    with pytest.raises(AssertionError) as e:
        getMinMax(List4, "MID")
    assert e.typename == "AssertionError", "Should raise  AssertionError!"

def test_getMinMaxEmptyError():
    List5 = []
    initializeMinMaxList(List5)
    with pytest.raises(AssertionError) as e:
        getMinMax(List5, "MAX")
    assert e.typename == "AssertionError", "Should raise  AssertionError!"






