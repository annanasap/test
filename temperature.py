#Fahrenheit Celsius converter

#Aks temperature:
tempF = input("What's the temperature in Fahrenheit?: ")
tempF = float(tempF)

#convert to Fahrenheit
tempC = (tempF - 32) /1.8

print("The temperature in Celsius is: " + str(tempC))