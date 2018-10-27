#Quiz with 3 questions, percentage of answer correct at the bottom
correct = 0
answ = input("Welke maand vieren we Sinterklaas?: ")
if answ.lower() == "december":
    print("Goed!")
    correct += 1
else:
    print("Helaas, dombo")

answ = int(input("Hoeveel letters heeft het alfabet?: "))
if answ == 26:
    print("Goed zo!")
    correct += 1
else:
    print("Typfoutje? Jammer!")

answ = input("Is Python een leuke taal? y//n: " )
if answ == "y":
    print("Weet je dat nu al? Goed hoor")
    correct += 1
else:
    print("waarom doe je deze quiz? Helaas!")

answ = input("Waarom heeft haarlem zoveel kappers? " )
if answ == "Omdat het haarlem heet":
    print("Jaja.. Goed!")
    correct += 1
else:
    print("Kijk naar de naam; logisch toch?")
print("Je hebt in totaal " + str(correct / 4) + "% van de vragen goed")
