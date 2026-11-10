for x in range(7):
    for y in range(6 - x):
        print(" ", end=" ")
    for y in range(7):
        if x == 0 or x == 6 or y == 0 or y == 6:
            print("*", end=" ")
        else:
            print("  ", end=" ")
    print(" ")
