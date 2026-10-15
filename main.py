def super_check_winner():
    for i in range(3):
        if area[0][0] == area[0][1] == area[0][2]:
            print(f"Победа {area[0][0]}")
            return area[0][0]

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

area = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
]

move = "X"

print_area()

for i in range(1, 10):
    if i % 2 == 0:
        move = "0"
        print("Ходят нолики")
    else:
        move = "X"
        print("Ходят крестики")

    row = int(input("Введите индекс строки (1 строчка - 0, 2 строчка - 1, 3 строчка - 2): "))
    column = int(input("Введите индекс столбца (1 столбец - 0, 2 столбец - 1, 3 столбец - 2): "))

    if area[row][column] == "*":
        area[row][column] = move
    else:
        print("\nЭто ячейка занята, не получится походить. Вы пропускаете ход.")


    print_area()

    winner = super_check_winner()

    if winner == "0" or  winner == "X":
        break

    if i == 9 and winner == "*":
        print("Ничья")
        break


print("Внимание говорит Москва Игра окончена")