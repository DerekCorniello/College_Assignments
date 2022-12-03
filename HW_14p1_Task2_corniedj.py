# Homework 14.1: Python Repitition
# File: HW_14p1_Task2_corniedj.py 
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
# Purpose: Simulate a two player dice game

import random

#set Variables
dice1 = 0
dice2 = 0
p1score = 0
p2score = 0

#set to player 1 turn, turn = 2 indicates player 2 turn
turn = 1

#Makes sure score is under 50
while (p1score < 50 and p2score < 50):
    
    #reset dice
    #if we left this value alone, 5 would ruin the rest of the loop and it would infinitely repeat
    dice1 = 0
    dice2 = 0
    
    if (turn == 1):
        print("Player 1's Turn \n")

        #Makes sure a die hasn't rolled a 5 and that the score is till under 50
        while(dice1 != 5 and dice2 != 5 and p1score < 50):

            #Randomize dice
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)

            #print dice outcomes
            print("First Dice: {}. Second Dice: {}".format(dice1, dice2))

            #only adds score of dice to score if they aren't fives
            if(dice1 != 5 and dice2 != 5):
                p1score += (dice1 + dice2)
                print("Player 1's Score: {}.".format(p1score))

            #exit loop if a 5 is rolled
            else:
                exit

        #change turn
        turn = 2
        print("Player 1's Turn is now over. \n")

    else:
        print("Player 2's Turn \n")

        #Makes sure a die hasn't rolled a 5 and that the score is till under 50
        while(dice1 != 5 and dice2 != 5 and p2score < 50):

            #Randomize dice
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)

            #Print dice outcomes
            print("First Dice: {}. Second Dice: {}".format(dice1, dice2))

            #Only adds score of dice to score if they aren't fives
            if(dice1 != 5 and dice2 != 5):
                p2score += (dice1 + dice2)
                print("Player 2's Score: {}.".format(p2score))

            #exits if a 5 is rolled 
            else:
                exit
                
        #change turn
        turn = 1
        print("Player 2's Turn is now over. \n")
        

#Since we change the turn variable at the end of the turn rather than the beginning,
#the opposite of the turn would be the winner.

#Prints the final game message.

if (turn == 1):
    print("The winner is Player 2!")
else:
    print("The winner is Player 1!")

print("Player 1 Final Score: {}".format(p1score))
print("Player 2 Final Score: {}".format(p2score))
