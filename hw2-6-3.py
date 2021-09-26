# Author: SCT (ADMG) 9/26/21

text = input("Enter the number of free throws scored\n")

text2 = input("Enter the number of 2 pointers scored\n")

text3 = input("Enter the number of 3 pointers scored\n")

free = int(text)

two = int(text2) * 2

three = int(text3) * 3

total = free + two + three

total = str(total)

print("The player scored " + total + " points in the game.")


