# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team099_corniedj.py 
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
# Calculate the Reynold's Number with inputs of fluid velocity, typical length, dynamic velocity and density of the fluid.


V = float(input("Enter the fluid velocity in mi/hr: ")) 
L = float(input("Enter the typical length in in: "))
mu = float(input("Enter the dynamic velocity in lbs/(in*s): "))
rho = float(input("Enter the density of the fluid in lb/(in^3): "))

V = V * 0.44704
L = L * 0.0254
mu = mu * 17.8579673
rho = rho * 27679.9


Reynolds_Num = (rho*V*L)/mu

print("The Reynolds Number is {0:.2f}".format(Reynolds_Num))
