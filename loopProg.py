n = 10
for row in range(1, 10):
    for column in range(1, row+1):
        print(n, end =" ")
        n += 1
    print()

n = int(input("Aantal: "))
for row in range(n):
    if row == 0 or row == n-1:
        print("o" *(n+2))
    else:
        print("o" + " " * n + "o")

for row in range(n):
    for column in range(n-row, 0, -1):
        print(column, end=" ")
    for column in range(row*2):
        print(" ", end=" ")
    for column in range(row, n+1):
        print(column, end =" ")
    print()
