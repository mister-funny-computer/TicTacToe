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

def check_winner():

    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        print("Нолики победели!!!!!!!!!!!!!!!!!!!!!")
        return "0"

    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":
        print("Нолики победели!!!!!!!!!!!!!!!!!!!!!")
        return "0"

    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":
        print("Нолики победели!!!!!!!!!!!!!!!!!!!!!")
        return "0"

    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":
        print("Нолики победили!!!!!!!!!")
        return "0"

    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":
        print("Нолики победели!!!!!!!!!!!!!!!!!!!!!")
        return "0"

    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":
        print("Нолики победели!!!!!!!!!!!!!!!!!!!!!")
        return "0"

    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":
        print("Нолики победели!!!!!!!!!!!!!!!!!!!!!")
        return "0"

    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":
        print("Нолики победели!!!!!!!!!!!!!!!!!!!!!")
        return "0"

    if area[2][0] == "X" and area[1][1] == "X" and area[0][2] == "X":
        print("Крестики победили!!!!!!!!!!")
        return "X"

    if area[0][0] == "X" and area[1][1] == "X" and area[2][2] == "X":
        print("Крестики победили!!!!!!!!!!")
        return "X"

    if area[0][1] == "X" and area[1][1] == "X" and area[2][1] == "X":
        print("Крестики победили!!!!!!!!!!!")
        return "X"

    if area[0][0] == "X" and area[1][0] == "X" and area[2][0] == "X":
        print("Крестики победили!!!!!!!!!!")
        return "X"

    if area[0][2] == "X" and area[1][2] == "X" and area[2][2] == "X":
        print("Крестики победили!!!!!!!!!!")
        return "X"

    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        print("Крестики победили!!!!!!!!!!")
        return "X"

    if area[1][0] == "X" and area[1][1] == "X" and area[1][2] == "X":
        print("Крестики победили!!!!!!!!!!")
        return "X"

    if area[2][0] == "X" and area[2][1] == "X" and area[2][2] == "X":
        print("Крестики победили!!!!!!!!!!")
        return "X"

    return "*"


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
    if i % 2 == 0:
        move = "0"
        print("Ходят нолики")
    else:
        move = "X"
        print("Ходят крестики")

    row = int(input("Введите индекс строки (1 строчка - 0, 2 строчка - 1, 3 строчка - 2): "))
    column = int(input("Введите индекс столбца (1 столбец - 0, 2 столбец - 1, 3 столбец - 2): "))

    area[row][column] = move

    print_area()

    winner = check_winner()

    if winner == "0" or  winner == "X":
        break

    if i == 9 and winner == "*":
        print("Ничья")
        break


print("Внимание говорит Москва Игра окончена")