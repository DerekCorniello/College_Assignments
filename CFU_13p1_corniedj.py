# CFU 13.1
# File: CFU_13p1_corniedj.py 
# Date:    11 14 2022
# By:      Derek Corniello
# Section: 007
# Team:    099
# 
# ELECTRONIC SIGNATURE
# DC
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Purpose: CFU 13.1

view = str(input("Which view would you like to view? "))

if (view == "Front" or view == "front"):
    print("Height and Width")
elif(view == "Top" or view == "top"):
    print("Width and Depth")
elif(view == "Right" or view == "right"):
    print("Depth and Height")
else:
    print("Invalid view, please try again.")
