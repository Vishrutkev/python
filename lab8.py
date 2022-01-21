# Lab 8 #
# Author: Vishrut Kevadiya
# Email: vishrutk@my.yorku.ca
# Student ID: 219155290
# Section: B


from random import randint
from time import sleep


class Snail:
    Slist = ["__~@", "_~_@", "~__@"]

    def __init__(self, name):
        self.name = name.upper()
        assert len(self.name) == 2, "Snail's initials must be 2 characters"
        self.speed = (randint(1, 10)) / 10
        self.frame = 0
        self.pos = 0

    def move(self):
        self.pos = self.pos + self.speed
        self.frame = (self.frame + 1)
        if self.frame > 2:
            self.frame = 0

    def getIntPos(self):
        return (int(self.pos))

    def getName(self):
        return (self.name)

    def getStr(self):
        str = (" " * self.getIntPos())
        str = str + Snail.Slist[self.frame]
        str = str + (" " * (40 - self.getIntPos()))
        str = str + self.getName()
        return str


def getSnailList():
    N = int(input("How many snails are racing? "))
    List = []
    for i in range(N):
        ini = input("Snail {} two initials: ".format(i + 1))
        List.append(Snail(ini))
    return List


def runRace(snails):
    srace = input("Press enter to start race.")
    curtimestep = 1
    while True:
        cur = (40 * "-") + "Time " + str(curtimestep)
        print(cur)
        for SO in snails:
            print(SO.getStr())
            SO.move()
            initpos = SO.getIntPos()
            if (initpos > 39):
                print("Snail " + SO.getName() + " WON!")
                return

        sleep(0.2)
        curtimestep += 1


def main():
    playagain = "Y"
    while playagain == "Y":
        print("Snail Race...")
        snail = getSnailList()
        runRace(snail)
        playagain = input("Play again (Y)? ").upper()


if __name__ == "__main__":
    main()