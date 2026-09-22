area = ["*", "*", "*"]

#print(area)

area[1] = "X"
area[2] = "0"

for cell in area:
    #print(cell, end=" ")
    pass

print()
print()



area = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
]

def print_area():
    print()
    print("|-------|")
    for row in area:
        print("| ", end="")
        for cell in row:
            print(cell, end=" ")
        print("|")
    print("|-------|")
    print()

#area[2][2] = "X"

#row = area[1]
#row[1] = "0"

print_area()

move = "X"


for i in range(1, 10):
    row = int(input("Введите индекс строки (1 строчка - 0, 2 строчка - 1, 3 строчка - 2): "))
    column = int(input("Введите индекс столбца (1 столбец - 0, 2 столбец - 1, 3 столбец - 2): "))

    if i % 2 == 0:
        move = "0"
    else:
        move = "X"

    area[row][column] = move

    print_area()




