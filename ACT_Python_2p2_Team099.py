pH = int(input("Enter the pH "))

if(pH < 7 and pH >= 0):
    print("pH is acidic")
elif(pH == 7):
    print("pH is neutral")
elif(pH <= 14):
    print("pH is Basic")
else:
    print("pH is Invalid")

