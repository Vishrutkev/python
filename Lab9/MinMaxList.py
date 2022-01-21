######
# EECS1015 - York University
#
# Topic 10 - MinMaxList class
# Lab 9
# Author: Vishrut Kevadiya
# Email: vishrutk@my.yorku.ca
# Student ID: 219155290
# Section: B
#
####

class MinMaxList:

    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult=False / True):
        if len(self.listData) == 0:
            self.listData.append(item)
        elif item >= self.listData[-1]:
            self.listData.append(item)
        else:
            i = 0
            for i in range(len(self.listData)):
                if item > self.listData[i]:
                    i += 1
                    if item < self.listData[i]:
                        self.listData.insert(i, item)
                        print("Item ({}) inserted at location {}".format(item, i))
                        if printResult:
                            print(self.listData)

    def getMin(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[0]
        del self.listData[0]
        return result

    def getMax(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[-1]
        del self.listData[-1]
        return result

    def printList(self):
        print(self.listData)


# Main function is given.
def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])
    bList = MinMaxList([88, 0])
    print("Starting aList: ", aList.listData)
    print("Starting bList: ", bList.listData)

    min1 = aList.getMin("MIN")
    min2 = bList.getMin("MIN")
    print("MinMaxList minimum with aList is %d" % (min1))
    print("MinMaxList minimum with bList is %d" % (min2))

    aList.insertItem(97)
    bList.insertItem(3)
    print("Insert 97 to aList")
    print("Instert 3 to bList")

    max1 = aList.getMax("MAX")
    max2 = bList.getMax("MAX")
    print("MinMaxList maximum with aList is %d" % (max1))
    print("MinMaxList maximum with bList is %d" % (max2))


if __name__ == "__main__":
    main()