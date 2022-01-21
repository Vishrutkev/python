##############################
# Lab3  --- Starting code (you can cut-and-paste into pycharm)
# Author name: Vishrut Kevadiya
# Student ID: 219155290
# Email address: vishrutk@my.yorku.ca
# Section B
##############################

# Code for task 1 after this line
print("\n--- Task 1 ---: Compute Fare")

print("(1) One way or (2) round trip?")
one = int(input("Enter 1 or 2: "))
print("""Select age range: 
(1) Under 12 
(2) 13-64 
(3) 65 or older""")
a = ("Enter 1, 2 or 3: ")
b = int(input(a))

if (one == 1):
    if (b == 2):
        print("Total amount due: $1.80 [one way (full fare)]")
    elif (b < 2):
        print("Total amount due: $0.90 [one way (reduced fare)]")
    elif (b > 2):
        print("Total amount due: $0.90 [one way (reduced fare)]")
else:
    if (one == 2):
        if (b == 2):
            print("Total amount due: $3.50 [round trip (full fare)]")
        elif (b < 2):
            print("Total amount due: $1.75 [round trip (reduced far])]")
        elif (b > 2):
            print("Total amount due: $1.75 [round trip (reduced far])]")

        # Code for task 2 after this line
print("\n--- Task 2 ---: Parse string")

string = input("Input a string: ")

for i in range(0, len(string)):
    if (string[i] == " "):
        print(f"str{[i]}= SPACE")
    else:
        print("str[%d]= %s" %(i, string[i]))
string = string.replace(" ", "")
b = string[::-1]
print("Reverse no spaces: %s" % (b))

# Code for task 3 after this line
print("\n--- Task 3 ---: The maximum *even* number")

print("Keep entering positive integer")
print("To quit, input a negative integer")
num = int(input("Enter a number: "))
i = 1
for num in range(0, num):
    num = int(input("Enter a number: "))
    if (num % 2 == 0 and num > i):
        i = num
    elif (num < 0):
        print("The largest even number: %d" % (i))
        break
else:
    print("Largest even number: %d" % (i))

# Code for task 4 after this line
print("\n--- Task 4 ---: Better triangle draw")

msg = "Enter a size between 5 and 20: "
N = -1

while N < 5 or N > 20:
    N = int(input(msg))

for i in range(1, N + 1):
    a = ("\\")
    for j in range(1, i):
        a = "-" + a
    print(a)
b = a.replace("\\", "|")
c = "-" + b
print(c)
for k in range(N, 0, -1):
    a = ("/")
    for j in range(1, k):
        a = "-" + a
    print(a)

input("Press enter to quit.")