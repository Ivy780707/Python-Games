import random

# 建立遊戲介面與格式
def display_board(matrix):
    print('    a   b   c   d   e   f   g   h   i  ')
    for i in range(9):
        print('  '+'+---'*9+'+')
        print(i+1, end=' ')
        for j in range(9):
            if matrix[i][j]['revealed']:
                print(f'| {matrix[i][j]["value"]} ', end='')
            elif matrix[i][j]['flagged']:
                print('| F ', end='')
            else:
                print('|   ', end='')
            if j == 8:
                print('|')
    print('  '+'+---'*9+'+')

# 設置旗子
def set_flag(row, col, matrix):
    matrix[row][col]['flagged'] = not matrix[row][col]['flagged']

# 計算九宮格內的炸彈數
def count_mines(row, col, matrix):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < 9 and j >= 0 and j < 9 and matrix[i][j]['value'] == 'X':
                count += 1
    if count > 0:
        matrix[row][col]['value'] = str(count)
    else:
        matrix[row][col]['value'] = '0'

# 顯示輸入座標格的數字以及其周圍數字
def reveal_cell(row, col, matrix):
    if matrix[row][col]['flagged']:
        return
    if matrix[row][col]['revealed']:
        return
    matrix[row][col]['revealed'] = True
    if matrix[row][col]['value'] == '0':
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i >= 0 and i < 9 and j >= 0 and j < 9:
                    reveal_cell(i, j, matrix)

# 初始化遊戲
def initialize_game():
    matrix = [[{'value': ' ', 'revealed': False, 'flagged': False} for _ in range(9)] for _ in range(9)]
    return matrix

# 開始遊戲
def play_minesweeper():
    matrix = initialize_game()
    game_over = False
    flag_used=0
    #只要沒有Game over就持續迴圈
    while not game_over:
        display_board(matrix)
        first_move = input(f'Enter the cell({10-flag_used} mines left): ')
        flag_used+=1
        #錯誤輸入
        if len(first_move) != 2 or not first_move[0].isalpha() or not first_move[1].isdigit():
            print('Invalid cell. Please enter a valid cell.')
            continue
        #計算應顯示之座標
        col = ord(first_move[0].lower()) - 97
        row = int(first_move[1]) - 1

        if 0 <= row < 9 and 0 <= col < 9:
            mine_indexes = random.sample(range(81), 10)

            # 避免屬用者在一開始採到炸彈
            user_index = row * 9 + col
            if user_index in mine_indexes:
                mine_indexes.remove(user_index)

            for index in mine_indexes:
                r = index // 9
                c = index % 9
                matrix[r][c]['value'] = 'X'

            for i in range(9):
                for j in range(9):
                    if matrix[i][j]['value'] != 'X':
                        count_mines(i, j, matrix)

            reveal_cell(row, col, matrix)
        else:
            print('Invalid cell. Please enter a valid cell.')
            continue

        while not game_over:
            display_board(matrix)

            location = input(f'Enter the cell: ')

            if len(location) < 2 or len(location) > 3:
                print('Invalid cell. Please try again.')
                continue

            if location[-1] == 'f':
                # Set/remove flag
                col = ord(location[0]) - 97
                row = int(location[1]) - 1

                if 0 <= row < 9 and 0 <= col < 9:
                    set_flag(row, col, matrix)
                else:
                    print('Invalid cell. Please try again.')

            else:
                col = ord(location[0]) - 97
                row = int(location[1]) - 1

                if 0 <= row < 9 and 0 <= col < 9:
                    if matrix[row][col]['value'] == 'X':
                        # Game over, reveal all mines and remaining cells
                        for i in range(9):
                            for j in range(9):
                                if matrix[i][j]['value'] == 'X':
                                    matrix[i][j]['revealed'] = True
                                elif not matrix[i][j]['revealed']:
                                    reveal_cell(i, j, matrix)

                        display_board(matrix)
                        print('Game over')
                        break
                    else:
                        reveal_cell(row, col, matrix)
                        #贏的條件
                        if all(matrix[i][j]['revealed'] or matrix[i][j]['value'] == 'X' for i in range(9) for j in range(9)):
                            display_board(matrix)
                            print('Win')
                            break
                else:
                    print('Invalid cell. Please try again.')

        #遊戲結束後問使用者要不要再玩一次
        play_again = input('Play again? (yes/no): ')
        if play_again.lower() == 'yes':
            matrix = initialize_game()
            game_over = False
        else:
            game_over = True

# Start the game
play_minesweeper()
