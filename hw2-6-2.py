# Author: SCT (ADMG) 9/26/21

text = input("Enter radius of cylinder")

text2 = input("Enter height of cylinder")

radius = int(text)

height = int(text2)

Volume = (3.14) * (radius ** 2) *height

Volume = str(Volume)

print("Volume = " + Volume)

Surface_Area = 2 * 3.14 * radius * (height + radius)

Surface_Area = str(Surface_Area)

print("Surface Area = " + Surface_Area)


