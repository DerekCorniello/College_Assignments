# Activity: Python Repetition
# File: ACT_Python_3p2_Team099.py 
# Date:    11 21 2022
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
# Purpose: Display the odds of a coin flipped on heads based on randomness

import random

num = int(input("How many times should we flip the coin? "))

heads = 0
k = 0

for k in range(0, num):
    flip = random.randint(0,1)
    if (flip == 1):
        heads += 1

tails = num-heads

print("The percentage of heads is: {0:.2f}%".format((heads/num)*100))
print("The percentage of heads is: {0:.2f}%".format((tails/num)*100))
