# Homework 11.1: Python Sequential
# File: HW_11p1_Task2_UCusername.py 
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
# Purpose: Calculate Velocity in in/s given mass in kg, K, and initial velocity in m/s
import math

Vo = float(input("Enter the initial speed (Vo, m/s): "))
K = float(input("Enter the constant (K, Kg*m^2/s): "))
m = float(input("Enter the mass of the mobile (m, Kg): "))

V = math.sqrt(((39.4*Vo)**2)-((15477.02*K)/(.07*m)))

print("The Value of V={0:.2f} in/s".format(V))
