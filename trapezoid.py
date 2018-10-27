#Find the area of a trapezoid:

height = float(input("Enter height of trapezoid: "))
lengthBottom = float(input("Enter the length of the bottom base: "))
lengthTop = float(input("Enter the length of the top base: "))

area = 0.5 * (lengthBottom + lengthTop) * height
print("The area is: " + str(area))