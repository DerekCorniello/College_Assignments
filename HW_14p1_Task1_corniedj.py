# Homework 14.1: Python Repitition
# File: HW_14p1_Task1_corniedj.py 
# Date:    11 25 2022
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
# Purpose: Randomly guess a four digit code and output the number of guesses
# that meet certain conditions

import random

#Grab Inputs
N1 = int(input("Write the first digit of your code: "))
N2 = int(input("Write the second digit of your code: "))
N3 = int(input("Write the third digit of your code: "))
N4 = int(input("Write the fourth digit of your code: "))

input("\nWhen you are ready, press 'enter' to begin the guessing process. \n")

#Set starting Values for summing variables
oneDigit = 0
twoDigit = 0
threeDigit = 0
fourDigit = 0
noDigit = 0
    
for i in range(0, 1000, 1):

    #Reset all Variables
    G1 = random.randint(0,9)
    G2 = random.randint(0,9)
    G3 = random.randint(0,9)
    G4 = random.randint(0,9)
    num_right = 0

    #Compare random numbers to known numbers and tally them
    if (G1 == N1):
        num_right += 1
    if (G2 == N2):
        num_right += 1
    if (G3 == N3):
        num_right += 1
    if (G4 == N4):
        num_right += 1

    #Categorize them by numbers correct
    if (num_right == 1):
        oneDigit += 1
    elif (num_right == 2):
        twoDigit += 1
    elif (num_right == 3):
        threeDigit += 1
    elif (num_right == 4):
        fourDigit += 1
    else:
        noDigit +=1

#Add categories to list
digitList = [noDigit, oneDigit, twoDigit, threeDigit, fourDigit]

#Display lists
for j in range(0,5):
    print("The number of guesses with exactly {} correct digits is {}.".format(j, digitList[j]))
