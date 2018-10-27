# The famous Camel game, made in python by Anna!
# 19 Ocotber 2018

import random

#Game instructions
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")

#Variables
done = False
milesTraveled = 0
thirst = 0
camelTiredness = 0
distNatives = -20
nDrinks = 3

#Main loop
while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    userInput = input("What would you like to do?: ")
    print()

# Quit the game
    if userInput.lower() == "q":
        done = True
        print("ok doei")

# Status update
    elif userInput.lower() == "e":
        print("Miles traveled: " + str(milesTraveled))
        print("Drinks in canteen: " + str(nDrinks))
        print("The natives are " + str(distNatives) + " miles behind you.")
        print()
        done = False

# Rest the camel
    elif userInput.lower() == "d":
        camelTiredness = 0 # reset to zero
        distNatives += random.randrange(0, 15)
        print("The camel is happy!")
        print("The natives are " + str(distNatives) + " miles behind you.")
        print()
        done = False

 # Full speed ahead   
    elif userInput.lower() == "c":
        milesTraveled += random.randrange(10, 21)
        thirst += 1
        camelTiredness += random.randrange(1, 3)
        distNatives += random.randrange(0, 10)
        print("the camel traveled " + str(milesTraveled) + " miles")
        print()

# Moderate speed  
    elif userInput.lower() == "b":
        milesTraveled += random.randrange(2, 15)
        thirst += 1
        camelTiredness += 1
        distNatives += random.randrange(0, 10)
        print("The camel traveled " + str(milesTraveled) + " miles")
    

# Drink from canteen  
    elif userInput.lower() == "a":
        if thirst > 8:
            print("Your camel is dead")
            done = True
        elif thirst > 6:
            print("You died of thirst!")
            done = True     
        elif thirst > 4:
            nDrinks -= 1
            thirst = 0
            print("You are thirsty!")
            distNatives += random.randrange(0, 10)
        elif nDrinks == 0:
            print("There are no more drinks available!")
        else:
            nDrinks -= 1
            thirst = 0
            distNatives += random.randrange(0, 10)
            print("Refreshing!")

# Traveled 200 miles and won   
    if not done and milesTraveled == 200:
        print("Congratulations, you won!")
        done = True

# Tiredness too high
    elif not done and camelTiredness > 8:
        print("Your camel is dead")
        done = True

# Tiredness high warning
    elif not done and camelTiredness > 5:
        print("Your camel is getting tired")

# Natives have caught up 
    elif not done and distNatives == 0:
        print("The natives have caught up and captured you. Game over!")
        done = True

# Natives are getting close 
    elif not done and distNatives < 15:
        print("The natives are getting close!")
        done = False      

# Random change you found an oasis
    elif not done and random.randrange(1, 21) == 20:
        print("You found an oasis!")
        print("Your canteen has been refilled")
        print("You have stilled your thirst")
        print("And it's time to relax!")
        thirst = 0
        camelTiredness = 0
        nDrinks = 3
    

    
    
