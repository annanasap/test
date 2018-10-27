# Ask for personal data and output
#print("What's your name?")
#myName = input()
#print("Thanks, " + myName)
#print("The length of your name is " + str(len(myName)))
#print("What's you age?")
#myAge = input()
#myAge = int(myAge)
#print("Next year, you'll be " + str(myAge + 1))

#password
while True:
    print("Who are you?")
    name = input()
    if name != "Anna": #wanneer de naam niet Anna is gaat ie weer terug naar de eerste vraag
        continue
    print("Hello Anna, what's the password? (it is a fish)")
    password = input()
    if password == "swordfish":
        break # alleen wanneer het password OK is print hij het statement, anders weer naar begin vd loop
print("access granted")