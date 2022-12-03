# Homework 11.1: Python Sequential
# File: HW_11p1_Task1_UCusername.py 
# Date:    11 4 2022
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
# Calculates "Gam", 'q' and 'p' from the speed of light, mobile, and mass of mobile

import math

c = float(input("Enter the speed of light, c in m/s "))
v = float(input("Enter the speed of the mobile, v in m/s "))
m = float(input("Enter the mass of the mobile, m in kg "))

Gam = 1/(math.sqrt(1-(v/c)**2))

p = m*v
q = m*v*Gam

print("\nGam = {0:.2f}".format(Gam))
print("p = {0:.2e}kg*m/s".format(p))
print("q = {0:.2e}kg*m/s".format(q))
