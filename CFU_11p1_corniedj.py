# CFU 11.1
# File:    CFU_11p1_corniedj.py
# Date:    10 31 2022
# By:      Derek Corniello
# Section: 007
# Team:    099
# 
# ELECTRONIC SIGNATURE
# Derek Corniello
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Calculates the velocity based off the launch angle, range,
# and acceleration due to gravity on a projectile

import math

#Grab inputs

g = float(input("Input the acceleration due to gravity in m/s: "))
degrees_measure = float(input("Input the angle measure of the trajectory, in degrees: "))
R = float(input("Input the horizontal distance, or range, of the projectile: "))

#change the degreees to radians to adjust for sin function

radian_measure = math.radians(degrees_measure)

#Calculate the velocity

V = math.sqrt((R*g)/(math.sin(radian_measure)**2))

print("The Velocity is {0:.2f}".format(V))
