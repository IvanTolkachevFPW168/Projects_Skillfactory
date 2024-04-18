
# Приветствие и название игры
print('*' * 10, ' Здравствуйте! Это Игра Крестики-нолики для двух игроков!', '*' * 10)

# Инициализация карты
maps = list(range(1, 10))

# Победные линии
win_victories = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

# Выводим карту на экран
def drow_maps():
    print('-' * 15)
    for i in range(3):
        print('[', maps[0 + i * 3], '][', maps[1 + i * 3], '][', maps[2 + i * 3], ']')
        print('-' * 15)

# Делаем ход в выбранную ячейку
def step_maps(step, sym):
    index = maps.index(step)
    maps[index] = sym

# Получаем текущий результат игры
def result_get():
    winer = ''
    for i in win_victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            winer = 'X'
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            winer = 'O'
    return winer

# Основой блок программы
Count = 0
Game_over = False
Player1 = True

while Game_over == False:
    # 1) Открываем карту
    drow_maps()
    # 2) Спрашиваем у игрока куда делать ход
    if Player1 == True:
        sym = "X"
        step = int(input("Игрок 1, ваш ход: "))
        if step >= 1 and step <= 9:
            if (str(maps[step-1])) not in 'XO':
                maps[step-1] = step
            else:
                print("Эта клетка уже занята!")
                continue
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue
        Count += 1
    else:
        sym = "O"
        step = int(input("Игрок 2, ваш ход: "))
        if step >= 1 and step <= 9:
            if (str(maps[step-1])) not in 'XO':
                maps[step-1] = step
            else:
                print("Эта клетка уже занята!")
                continue
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue
        Count += 1
    step_maps(step, sym)  # Делаем ход в выбранную ячейку
    winer = result_get()  # Определим победителя
    if Count > 4:
        winer = result_get()
        if winer:
            drow_maps()
            print('Победителем является: ', winer)
            win = True
            break
    if Count == 9:
        drow_maps()
        print("Ничья!")
        break
    Player1 = not (Player1)
# После окончания игры. Показываем карту. Объявляем победителя.

