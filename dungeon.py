room_list = []

# Kamers
room = ["Je bent in de eetkamer.\nEr is een ingang naar het noorden.", 3, 1, None, None]
room_list.append(room)
room = ["Je bent in de hal.\nVanaf hier kun je drie kanten op.", 4, 2, None, 0]
room_list.append(room)
room = ["Welkom in de woonkamer, aan de voorkant van het huis.\nJe kunt niet naar het noorden, wel naar het westen.", 5, None, None, 1]
room_list.append(room)
room = ["Sst! Je bent in de slaapkamer!\nEr zijn deuren naar het oosten en zuiden.", None, 4, 0, None]
room_list.append(room)
room = ["Lekker koken in de keuken.\nOostwaards kun je niet.", None, None, 1, 3]
room_list.append(room)
room = ["In de hoek van het huis is deze tweede slaapkamer.\nJe kunt niet direct naar de keuken wandelen!", None, None, 2, None]
room_list.append(room)

current_room = 0

done = False

while not done:
    print()
    print(room_list[current_room][0])
    userInput = input("Welke richting? ")
    print()

# Quit the game
    if userInput.lower() == "q":
        done = True
        print("ok doei")

# Noordwaarts
    elif userInput.lower() == "n" or userInput.lower() == "noord":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("Die kant kun je niet op.")
        else:
            current_room = next_room

# Oostwaarts    
    elif userInput.lower() == "o" or userInput.lower() == "oost":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("Die kant kun je niet op.")
        else:
            current_room = next_room
# Zuidwaarts
    elif userInput.lower() == "z" or userInput.lower() == "zuid":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("Die kant kun je niet op.")
        else:
            current_room = next_room
# Westwaarts
    elif userInput.lower() == "w" or userInput.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("Die kant kun je niet op.")
        else:
            current_room = next_room

# Verkeerde input
    else:
        print("Ik snap niet wat je hebt getypt.")