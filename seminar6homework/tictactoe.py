# Крестики нолики


def new_board():
    board=[[0 for _ in range(3)] for _ in range(3)] #пустая доска
    return board

def print_board(board: list): #Печатаем доску
    for item in board:  #если 0, то прочерк. Если меньше 0 то Х, иначе О
        print('|'.join(map(lambda x: "-" if x==0 else ("X" if x < 0 else "O"),item)))

def make_move(board:list,x:int,y:int, move:int):
    if x>=1 and x<=3 and y>=1 and y<=3:
        if board[x-1,y-1]==0:
            board[x-1,y-1]=move
            return True #Успешный ход
    return False #Хода нет

board=new_board()

print_board(board)
