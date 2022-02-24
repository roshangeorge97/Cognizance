n=5
for row in range(0,n):
    for space in range(0,n-row):
        print(" ", end="")
    for coloumn in range(0,row+1):
        print(" *", end="")
    print()


