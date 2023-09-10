# Крестики нолики


def new_board():
    board=[[0 for _ in range(3)] for _ in range(3)] #пустая доска
    return board

def print_board(board: list): #Печатаем доску
    for item in board:  #если 0, то прочерк. Если меньше 0 то Х, иначе О
        print('|'.join(map(lambda x: "-" if x==0 else ("X" if x < 0 else "O"),item)))

board=new_board()
print_board(board)
