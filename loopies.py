'''
for row in range(10):
    for column in range(row+1):
        print(" ", end = " ")
    for column in range(10-row):
        print(column, end = " ")
    print()

for row in range(1, 10):
    for column in range(1, 10):
        if row*column < 10:
            print(" ",end = "")
        print(row*column,end = " ")
    print()

'''
# Een ruit van cijfers!
for row in range(1, 10):
    for column in range(10-row):
        print(" ", end=" ")
    for column in range(1, row+1):
        print(column, end = " ")
    for column in range(row-1, 0, -1):
        print(column, end = " ")
    print()

for row in range(10):
    for column in range(row+2):
        print(" ", end = " ")
    for column in range(1, 9-row):
        print(column, end = " ")
    for column in range(7-row, 0, -1):
        print(column, end= " ")
    
    print()
