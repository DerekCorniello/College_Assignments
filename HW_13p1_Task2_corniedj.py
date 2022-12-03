# Homework 13.1: Python Conditional
# File: HW_13p1_Task2_corniedj.py 
# Date:    11 18 2022
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
# Purpose: Calculate the density of an inputted metal and it's believed structure
# and determine if it is the actual structure.
import sys
import math

metalName = input("Enter the name of the metal (Al, Co or Cr): ")

if (metalName == "Al"):
    molarMass = 26.98
    R = .1431*10**(-7)
    actDensity = 2.7
elif(metalName == "Co"):
    molarMass = 58.93
    R = .1253*10**(-7)
    actDensity = 8.9
elif(metalName == "Cr"):
    molarMass = 52.00
    R = .1249*10**(-7)
    actDensity = 7.2
else:
    print("Invalid Entry, please try again")
    sys.exit()


massOfAtom = molarMass/(6.022*10**(23))


structure = input("Enter a crystal structure (BCC, FCC or HCP): ")

if(structure == "FCC"):
    a = (4*R)/math.sqrt(2)
    volume = a**3
    numAtoms = 4
elif(structure == "BCC"):
    a = (4*R)/math.sqrt(3)
    volume = a**3
    numAtoms = 2
elif(structure == "HCP"):
    a = 2*R
    c = 1.63*a
    volume = (3*math.sqrt(3)*c*a**(2))/2
    numAtoms = 6
else:
    print("Invalid Entry, please try again")
    sys.exit()

calculatedDensity = (massOfAtom*numAtoms)/volume

percentDifference = abs(actDensity-calculatedDensity)/actDensity

print("The calculated density of {} with {} structure is ".format(metalName, structure) + "{0:.2f} g/cm^3.".format(calculatedDensity))

if(percentDifference <= .05):
    print("The difference is <= 5%, thus {} is the right crystal structure".format(structure))
else:
    print("The density difference is > 5 percent, thus {} may not be the right crystal structure.".format(structure))
