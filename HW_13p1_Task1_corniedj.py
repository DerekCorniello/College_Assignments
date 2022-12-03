# Homework 13.1: Python Conditional
# File: HW_13p1_Task1_corniedj.py 
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
# Purpose: Use Pressure and Temperature to find the matter state of water
import math

P = float(input("Input the pressure in atm: "))
T = float(input("Input the temperature in Celcius: ")) + 273.15

P1 = 0.006*math.exp(6293*((1/273.15)-(1/T))-0.56*math.log(T/273.15))
P2 = 0.006*math.exp(6808*((1/273.15)-(1/T))-5.09*math.log(T/273.15))

if(T>647 and P>218):
    print("super critical liquid")
elif(T<273.15):
    if(P>P1):
        print("solid/ice")
    else:
        print("gas/vapor")
elif(P>P2):
    print("liquid/water")
else:
    print("gas/vapor")
