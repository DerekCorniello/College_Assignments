# Homework 11.1: Python Sequential
# File: HW_11p1_Task3_UCusername.py 
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
# Purpose: Find the amplitude of the reflected and transmitted wave for an oblique incidence

import math

E_i = float(input("Enter the amplitude of the incident wave "))
n_one = float(input("Enter the intrinsic impedance of medium 1 "))
n_two = float(input("Enter the intrinsic impedance of medium 2 "))
theta_i = math.radians(float(input("Enter the angle of the incident wave (in Degrees) ")))
theta_t = math.radians(float(input("Enter the angle of the transmitted wave (in Degrees) ")))

E_t = float(E_i*((2*n_two*math.cos(theta_i))/(n_two*math.cos(theta_t)+n_one*math.cos(theta_i))))
E_r = float(E_i*((n_two*math.cos(theta_i)-n_one*math.cos(theta_t))/(n_two*math.cos(theta_i)+n_one*math.cos(theta_t))))

print("\nThe amplitude of the transmitted wave is E_t = {0:.2f} V/m".format(E_t))
print("The amplitude of the reflected wave E_r = {0:.2f} V/m".format(E_r))
