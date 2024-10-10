#question2
#using a function, create a program that calculates the volume of a cylinder
radius = 6
height = 14
pie = 3.14
volume = (pie*radius**2*height)
print(f"The volume of a cylinder of radius {radius} and height {height} is {volume:.2f}\n")
#alternatively
import math
pie = math.pi
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))
volume = (pie*radius**2*height)
print(f"The volume of a cylinder of radius {radius} and height {height} is {volume:.2f}\n")
