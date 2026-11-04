size = int(input("Input size: ")) 

for x in range(size // 2 + 1):
    lines = " " * (size // 2 - x)
    stars = "* " * (x + 1)
    print(lines + stars)
    

for y in range(size // 2 - 1, -1, -1):
    lines = " " * (size // 2 - y)
    stars = "* " * (y + 1)
    print(lines + stars)

