area = ["*", "*", "*"]

print(area)

area[1] = "X"
area[2] = "0"

for cell in area:
    print(cell, end=" ")

print()
print()

area = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
]

area[2][2] = "X"

row = area[1]
row[1] = "0"

print("|-------|")
for row in area:
    print("| ", end="")
    for cell in row:
        print(cell, end=" ")
    print("|")
print("|-------|")


row = input("Введите индекс строки (1 строчка - 0, 2 строчка - 1, 3 строчка - 2): ")
column = input("Введите индекс столбца (1 столбец - 0, 2 столбец - 1, 3 столбец - 2): ")

area[row][column] = "X"