k_1 = float(input("Spring Constant 1 N/m: "))
k_2 = float(input("Spring Constant 2 N/m: "))
F_total = float(input("Total Force in N: "))
config = str(input("Parallel or Series (enter p, s, parallel, or series): "))

if(k_1 < 0 or k_2 < 0 or F_total < 0):
    print("One or more of your inputs are invalid, please try again")

elif (config == "p" or config == "parallel"):
    k_eq = k_1 + k_2
    
    x = F_total / k_eq
    x_1 = x
    x_2 = x_1

    F_1 = k_1 * x_1
    F_2 = k_2 * x_2
    
else:
    k_eq = (k_1*k_2)/(k_1*k_2)
    
    F_1 = F_total
    F_2 = F_1

    x = F_total / k_eq
    x_1 = F_1 / k_1
    x_2 = F_2 / k_2

print("k_eq in N/m = (0:.2f)".format(k_eq))
print("F_1 in N/m = (0:.2f)".format(F_1))
print("F_2 in N/m = (0:.2f)".format(F_2))
print("x_1 in N/m = (0:.2f)".format(x_1))
print("x_2 in N/m = (0:.2f)".format(x_2))
