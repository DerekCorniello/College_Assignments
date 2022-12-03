# CFU 14.1: Python Repition
# File: CFU_14p1_TEAM099.py 
# Date:    11 21 2022
# By:      Team 099
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
# Purpose: Outputs GCF of two inputted integers

int_1 = int(input("Enter the first integer: "))
int_2 = int(input("Enter the second integer: "))

if(int_1>0 and int_2>0):
    if (int_1 < int_2):
        small_num = int_1
    elif (int_1 > int_2):
        small_num = int_2
    else:
        print("The GCF for this is {0}".format(int_1))
    for k in range(1, small_num + 1, 1):
        mod_1 = int_1%k
        mod_2 = int_2%k

        if (mod_1 == 0 and mod_2 == 0):
            GCF = k
    print("The GCF is {0}.".format(GCF))
else:
    print("Please enter 2 positive, non-zero integers.")
