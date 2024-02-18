yesno = input('Do you want to play tictactoe')
start = yesno == 'Y'
exit = yesno == 'N'
# write Y for start or N to exit
game_field = [[" "] * 3 for i in range(3)]


def show():
    print(f'  0 1 2')
    for i in range(3):
        row_info = " ".join(game_field[i])
        print(f"{i} {row_info}")


def ask():
    while True:
        x, y = map(int, input('Your turn: ').split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if game_field[x][y] == " ":
                return x, y
            else:
                print('Клетка занята!')
        else:
            print('Вы зашли за координатную черту!')


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(game_field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print('X WIN !!!')
            return True
        if symbols == ["O", "O", "O"]:
            print('O WIN!!!')
            return True
    return False


num = 0
while True:
    if start:
        num += 1
        show()
        if num % 2 == 1:
            print('Ходит X')
        else:
            print('Ходит O')
        x, y = ask()
        if num % 2 == 1:
            game_field[x][y] = "X"
        else:
            game_field[x][y] = "O"
        if win():
            break
    if num == 9:
        print('Ничья')
        break
