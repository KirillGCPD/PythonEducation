# Крестики нолики

ai_level=20
globi=0
def new_board():
    board=[[0 for _ in range(3)] for _ in range(3)] #пустая доска
    return board

def print_board(board: list): #Печатаем доску
    for item in board:  #если 0, то прочерк. Если меньше 0 то Х, иначе О
        print('|'.join(map(lambda x: "-" if x==0 else ("X" if x < 0 else "O"),item)))

def make_move(board:list, xy, player:int=1): #Делаем ход move = 1 если О
    x=xy[0] 
    y=xy[1]
    if x>=0 and x<=2 and y>=0 and y<=2:
        if board[x][y]==0:
            board[x][y]=player
            return True #Успешный ход
    return False #Хода нет

def is_win(board,player:int=1): #Проверяем выиграл ли игрок
    for row in board:
        if row.count(player) ==3: #три в ряд
            return True
    for i in range(3):
        score=0
        for j in range(3):
            if board[j][i]==player: #три про столбцам
                score += 1
        if score==3:
            return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player: #перекрестие
        return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        return True
    return False #в остальных случаях у нас False
def inverse_player(player):
    if player==1:
        return -1
    if player==-1:
        return 1
    return 0

def score_board(board): #оценка доски
    if is_win(board,1): #выиграл нолик
        return 100
    if is_win(board,-1): #Выиграл крестик
        return -100 #очень плохая оценка
    return 0 #ничья?

def generate_moves(board): #Все доступные ходы
    moves=list()
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                moves.append((i,j))
    return moves

def copyboard(board): #копировать доску
    new_board=[[0 for _ in range(3)] for _ in range(3)] #пустая доска
    for i in range(3):
        for j in range(3):
            new_board[i][j]=board[i][j]
    return new_board

def game_is_over(board):
    moves=generate_moves(board)
    if len(moves)==0:
        return True
    if is_win(board,-1):
        return True
    if is_win(board,1):
        return True
    return False

def ask_player_move(board,player=-1):
    is_moved=False
    while is_moved!=True:
        try:
            x=int(input("Введите ряд: "))    
            y=int(input("Введите столбец: "))
            x-=1
            y-=1
            is_moved = make_move(board,(x,y),player)
            if not is_moved:
                print("Ход не удался, попробуйте еще раз")
        except:
            print("Вы ввели некорректное значение, попробуйте еще раз")

def minimax(board,is_max:bool=True):
    if game_is_over(board):
        return [score_board(board),(-1,-1)]
    moves=generate_moves(board)
    best_value=0
    if is_max:
        best_value=-1000000
    else:
        best_value=1000000
    best_move=(-1,-1)
    minimax_result=[0,(-1,-1)]
    for move in moves:
        new_board=copyboard(board)
        p=0
        if is_max:
            p=1
        else:
            p=-1
        make_move(new_board,move,p)
        minimax_result=minimax(new_board,not is_max)
        if is_max:
            if minimax_result[0]>best_value:
                best_value=minimax_result[0]
                best_move=move
        else:
             if minimax_result[0]<best_value:
                best_value=minimax_result[0]
                best_move=move        
       
    return [best_value,best_move]
def game_result(board):
    if is_win(board,-1):
        return "Поздравляю - вы победили!"
    if is_win(board,1):
        return "К сожалению, вы приграли"
    return "Ничья"
    
board=new_board() #Новая доска
print_board(board)
while not game_is_over(board): #пока у нас нет геймовера последовательно  
    ask_player_move(board) #спрашиваем ход пользователя
    print_board(board) 
    if game_is_over(board): #если конец то выводим результат
        print(game_result(board))
        break
    val=minimax(board,1) #вклчаем алгоритм minimax 
    print(val)
    make_move(board,val[1],1)
    print_board(board)
    if game_is_over(board):
        print(game_result(board))
        break
