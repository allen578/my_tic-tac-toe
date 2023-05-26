import time

# 终端下井字棋

# 放棋子的棋盘
#board = [" " for i in range(10)]
board = ["None", " ", " ", " ", " ", " ", " ", " ", " ", " "]
# 进行参照的棋盘
num_board = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]


def minimax(board, now, root):
    """
    用来计算当前的最优落子的位置
    board : 棋盘
    now :   当前是 X 还是 O
    root :  根节点是 X 还是 O
    """
    # 递归出口
    if board.count(" ") == 0:    # 表明棋盘被下满了
        return 0
    else:
        if check_win_quiet(board):  # 表明有人赢了
            if now == root:  # 当前的和根结点是同一个，那么就代表输了，因为无子可下了。
                return -1
            else:            # 当前的和根节点不是同一个，那么就代表赢了，因为对方无子可下了。
                return 1  
    
    if now == root:   # 当前步应该是取max
        step, init = 0, -10
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = now   # 这一步的落子位置
                now = "X" if now =="O" else "O" # 对now进行切换
                score = minimax(board, now, root)
                if init <= score:   # 如果更优
                    init = score
                    step = i
                board[i] = " "
                now = "X" if now =="O" else "O"  # 将now换回来
        return init
    
    if now != root:  # 当前步应该是取min
        step, init = 0, 10
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = now
                now = "X" if now == "O" else "O"
                score = minimax(board, now, root)
                if init >= score:
                    init = score
                    step = i
                board[i] = " "
                now = "X" if now == "O" else "O" # 将now换回来
        return init
            
def start_minimax(board, root):
    """
    minimax算法只是用来搜索出最优的分数的
    如果用图来解释的话, 该算法是在第二层开始实现, 而根结点那边需要定出最后的策略
    board : 当前的棋盘
    root : 这一步是 X 还是 O
    """
    score = -10  # 根结点是需要求出最大值的
    step = 0
    now = root
    for i in range(1, 10):
        if board[i] == " ":  # 当前位置可落子
            board[i] = now
            now = "X" if now == "O" else "O"  # 对now的转换
            tmp = minimax(board, now, root)
            if (tmp > score):
                score = tmp
                step = i
            now = "X" if now == "O" else "O"
            board[i] = " "
    return step
            
# 绘制棋盘
def display_board():
    """绘制出整个棋盘"""
    print(board[1] + " | " + board[2] + " | " + board[3] + f"            {num_board[1]} | {num_board[2]} | {num_board[3]}")
    print("---------          ------------")
    print(board[4] + " | " + board[5] + " | " + board[6] + f"            {num_board[4]} | {num_board[5]} | {num_board[6]}")
    print("---------          ------------")
    print(board[7] + " | " + board[8] + " | " + board[9] + f"            {num_board[7]} | {num_board[8]} | {num_board[9]}")
# 给AI大脑内部思考的玩意儿，因此要quiet，不能把AI思考的过程给显示出来(= =)
def check_win_quiet(board):
    '''
    检查是否有人已经赢了
    赢的标准: 相同的出现在同一条直线
    对于3 * 3 的棋盘来说, 一共有8条线
    '''
    flag = 0 # 初始化为0，如果变成1，就代表游戏结束了
    # 首先检查每一行
    if board[1] == board[2] and board[1] == board[3]:
        if board[1] == "X" or board[1] == "O":
            flag = 1
    elif board[4] == board[5] and board[4] == board[6]:  
        if board[4] == "X" or board[4] == "O":
            flag = 1
    elif board[7] == board[8] and board[7] == board[9]:
        if board[7] == "X" or board[7] == "O":
            flag = 1
    # 检查每一列
    elif board[1] == board[4] and board[1] == board[7]:
        if board[1] == "X" or board[1] == "O":
            flag = 1
    elif board[2] == board[5] and board[2] == board[8]:
        if board[2] == "X" or board[2] == "O":
            flag = 1
    elif board[3] == board[6] and board[3] == board[9]:
        if board[3] == "X" or board[3] == "O":
            flag = 1
    # 检查对角线
    elif board[1] == board[5] and board[1] == board[9]:
        if board[1] == "X" or board[1] == "O":
            flag = 1
    elif board[3] == board[5] and board[3] == board[7]:
        if board[3] == "X" or board[3] == "O":
            flag = 1
    
    if flag:
        return True
    else:
        return False
# 判断是否有一方已经赢了
def check_win(board):
    '''
    检查是否有人已经赢了
    赢的标准: 相同的出现在同一条直线
    对于3 * 3 的棋盘来说, 一共有8条线
    '''
    flag = 0 # 初始化为0，如果变成1，就代表游戏结束了
    # 首先检查每一行
    if board[1] == board[2] and board[1] == board[3]:
        if board[1] == "X" or board[1] == "O":
            print(board[1] + " win the game!")
            flag = 1
            display_board()
    elif board[4] == board[5] and board[4] == board[6]:  
        if board[4] == "X" or board[4] == "O":
            print(board[4] + " win the game!")
            flag = 1
            display_board()
    elif board[7] == board[8] and board[7] == board[9]:
        if board[7] == "X" or board[7] == "O":
            print(board[7] + " win the game!")
            flag = 1
            display_board()
    # 检查每一列
    elif board[1] == board[4] and board[1] == board[7]:
        if board[1] == "X" or board[1] == "O":
            print(board[1] + " win the game!")
            flag = 1
            display_board()
    elif board[2] == board[5] and board[2] == board[8]:
        if board[2] == "X" or board[2] == "O":
            print(board[2] + " win the game!")
            flag = 1
            display_board()
    elif board[3] == board[6] and board[3] == board[9]:
        if board[3] == "X" or board[3] == "O":
            print(board[3] + " win the game!")
            flag = 1
            display_board()
    # 检查对角线
    elif board[1] == board[5] and board[1] == board[9]:
        if board[1] == "X" or board[1] == "O":
            print(board[1] + " win the game !")
            flag = 1
            display_board()
    elif board[3] == board[5] and board[3] == board[7]:
        if board[3] == "X" or board[3] == "O":
            print(board[3] + " win the game ! ")
            flag = 1
            display_board()
    elif board.count(" ") == 0: # 表明棋盘已经被下满了，平局
        print("draw game !")
        display_board()
        flag = 1  # 平局代表游戏结束
    
    
    if flag:
        return True
    else:
        return False
       
# 玩家下棋
def put_cheese(player, name):
    """
    player放下一个棋子的过程
    player 是选手的字符串，为 'X' 或 'O'
    name 是选手的姓名
    """
    
    while True:
        num = input(name + ", Please input your decision (1 ~ 9): ")
        num = int(num)
        if board[num] != " ":  # 如果已经被占了
            print("your decision place has been taken, please consider another place!")
        else:  
            board[num] = player
            num_board[num] = " "
            break

# AI下棋
def AI_put(player):
    """
    AI 下一个棋子
    player : AI当前所处的角色
    """
    print("Now turn to the AI to play ! ")
    decision = 0  # AI最后决定的位置，初始化为0
    # 首先判断棋盘是否为空：如果为空，直接下在左上角
    if board.count(" ") == 9: # 棋盘为空，就将棋子固定在左上角
        board[1] = player  
        num_board[1] = " "
        return
    
    decision = start_minimax(board, player)
    board[decision] = player
    print("AI's choice is ", decision)
    num_board[decision] = " "
    
        
    
# 玩家对战
def player_vs_player():
    """
    双人对战
    """
    
    global board
    print("You have chosed the mode 1 : player vs player")
    player1 = input("Please tell me the first player name(use 'X') : ")
    player2 = input("Please tell me the second player name(use 'O') : ")
    print("Now the game start ! ")
    while True:
        
        display_board()
        put_cheese("X", player1)
        if check_win(board):
            break
        
        display_board()
        put_cheese("O", player2)
        if check_win(board):
            break
# 人机对战    
def player_vs_AI():
    """
    人机对战
    """
    global board
    print("You have chosed the mode 2 : player vs AI")
    choice = input("Which do you want to choose. 'X' or 'O' ? ")
    player1 = input("Please tell your name : ")
    print("Now the game start ! ")
    while True:
        if choice == "X":
            display_board()
            put_cheese("X", player1)
            if check_win(board):
                break
            
            display_board()
            time.sleep(1)
            AI_put("O")
            if check_win(board):
                break
        else:
            display_board()
            AI_put("X")
            if check_win(board):
                break
            
            display_board()
            put_cheese("O", player1)
            if check_win(board):
                break
# 电脑对战            
def AI_vs_AI():
    """
    机器人对战
    """
    global board
    print("You have chosed the mode 3 : AI vs AI")
    print(" This mode is set for having fun, just enjoy the game")
    print("Now the AI game Start ! ")
    while True:
        display_board()
        time.sleep(1)
        AI_put("X")
        if check_win(board):
            break
        
        display_board()
        time.sleep(1)
        AI_put("O")
        if check_win(board):
            break
  
 
       

if __name__ == "__main__":
    print("Welcome to the TIC TAC TOE game ! \n", 
          "Here are 3 modes: which modes do you want to play: \n",
          "     [1]  player vs player \n",
          "     [2]  player vs AI     \n",
          "     [3]  AI     vs AI")
    mode_choice = int(input("Please tell me your choice : "))  # 获取模式选择
    if mode_choice == 1:
        player_vs_player()
    elif mode_choice == 2:
        player_vs_AI()
    elif mode_choice == 3:
        AI_vs_AI()
    else:
        print("Our modes are limited in 1~3 ! ")
    
        
"""
启动页面样例：
    Welcome to the TIC TAC TOE game ! 
    The Game has started.
    Here are 3 modes: which modes do you want to play:
        [1]  player vs player
        [2]  player vs AI
        [3]  AI     vs AI
    Please tell me your choice : 
    
    (选择了1之后)
    You have chosed the mode 1 : player vs player 
    Please tell me the first player name(use 'X') :  allen
    Please tell me the second player name(use 'O') : cisco
    
    展示棋盘
    allen : 
    check_win()
    
    展示棋盘
    cisco : 
    check_win()
"""
        
