for i in range(3):
    for j in range(5): 
        if j >= 3 - i - 1 and j <= 2 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()