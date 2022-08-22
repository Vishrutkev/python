################
# Lab 2
# Author: Vishrut D. Kevadiya
# Email: vishrutk@my.yorku.ca
# Student ID: 219155290
# Section B
###############

print("\n----Task 1---- BMI Calculator")
## Write Task1 code here
name = input("Name: ")
a = name.strip().title()
weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))
b = (height/100)
bmi = weight/(b)**2
print("Name: {} Weight: {:.2f} Height [meters]: {:.2f} BMI: {:.2f}" .format(a, weight, b, bmi))

print("\n----Task 2---- Leetspeak Converter")
## Write Task2 code here
leetspeak = input("Type a lond string: ")
a = leetspeak.upper().strip().replace("T","+").replace("A","@").replace("E","3").replace("I","|").replace("B","8").replace("O","0").replace("C","[").replace("S","5")
print(a)

print("\n----Task 3---- Flipping String")
## Write Task3 code here
string = input("Input a Long String: ")
length = len(string)
middle = length//2
char = string[middle]
print(length)
print(middle)
print(char)
print(f"This string is {length} characters long")
print(f"The Middle Character is \"{char}\"")
upper = string.upper()
first = upper[middle:]
last = upper[:middle]
add = first + "|" + last
print("Flipped String")
print(add)



print("\n----Task 4---- MultiplY numbers")
## Write Task4 code here

number =input("input numbers to multiply: ")
number = number.strip()
number1 = number.find("*")
number2 = number[:number1]
number3 = number[number1+1:]
number5 = (number2+number3)
print("Extracted Number {}" .format(number5))
number6 = int(number2)
number7 = int(number3)
number8 = (number6*number7)
print(f"{number6} * {number7} = {number8}")


input("Press enter to exit. ")  # input statement to pause code when finished