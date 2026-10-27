size = int(input("input size of x -->"))

for x in range (size,):
    for y in range (size):
        if x + y == size  or x == y:
            print("*", end=" ")
        else:
            print("*", end=" ")
    print("*")