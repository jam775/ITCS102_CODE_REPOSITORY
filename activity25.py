def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x+1):
            print("*", end=" ")
        print()

def sum(x, y):
    return x+y

taga_triangle(5)
taga_triangle(8)
taga_triangle(12)
taga_triangle(10)

print(sum,(38, 5))
print(sum,(12, 7) *8)