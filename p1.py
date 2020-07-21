# Calvin Zug
# ctzug@wm.edu
# 7/10/2020
# Project 1: Conical Frustum Geometry
# 
# 
# This program will obtain three measures of a conical frustum inputted by the user, top radius, bottom radius, and height.
# Using these measurements, the program will be able to calculate and output the conical frustum's volume, slant height, and 
# surface area. The program will then thank the user and conclude.

# First we import the math library so we can use its functions for calculating later values
import math

# Here gets the users inputs for top radius, bottom radius, and height, converts them from strings into floats and then echos the user's inputs 
top_radius_str = input("Please enter the conical frustum's top radius ==> ")
top_radius_fl = float(top_radius_str)
print(top_radius_fl)
bot_radius_str = input("Please enter the conical frustum's bottom radius ==> ")
bot_radius_fl = float(bot_radius_str)
print(bot_radius_fl)
height_str = input("Please enter the conical frustum's height ==> ")
height_fl = float(height_str)
print(height_fl)


# This section calculates the volume, slant height, and surface area based off the users inputs from earlier
volume = (math.pi * height_fl) / 3 * (top_radius_fl ** 2 + bot_radius_fl ** 2 + (top_radius_fl * bot_radius_fl))
slant_height = math.sqrt((top_radius_fl - bot_radius_fl) ** 2 + height_fl ** 2)
surface_area = math.pi * (top_radius_fl ** 2 + bot_radius_fl ** 2 + slant_height * (top_radius_fl + bot_radius_fl)) 


# Finally the program prints out the 3 values the user inputted earlier along with the 3 new calculated values and formats it in a user friendly way. 
print("--------------------------------------------------")
print("")
print("     The conical frustum's top radius = {:8.3f}".format(top_radius_fl))
print("  The conical frustum's bottom radius = {:8.3f}".format(bot_radius_fl))
print("         The conical frustum's height = {:8.3f}".format(height_fl))
print("   The conical frustum's slant height = {:8.3f}".format(slant_height))
print("                               Volume = {:8.3f}".format(volume))
print("                         Surface Area = {:8.3f}".format(surface_area))
print("")
print("--------------------------------------------------")
print("")
print("Thank you for using this program.")