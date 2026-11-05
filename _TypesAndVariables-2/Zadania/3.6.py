###
# A program that calculates the distance to the horizon
# from a height given in meters from the keyboard.
#
import math
height = float(input("Enter observer height in meters: "))
distance = 3.57 * math.sqrt(height)
print(f"Distance to the horizon: {distance:.2f} km")
