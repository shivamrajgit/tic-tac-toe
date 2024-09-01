#TIC TAC TOE MADE BY SHIVAM


board=[["_","_","_"],["_","_","_"],["_","_","_"]]
def choices():
    while True:
        try:
            choice = int(input("Enter Row/Column no. (Between 1 and 3 only) :"))
            if choice>=1 and choice<=3:
                break
            else :
                print("Incorrect Row/Column no !!")
                continue
        except ValueError:
            print("Incorrect Row/Column no !!")
            continue
    return choice
def xTurn(board,turn):
    chance = "x"
    good = 0
    while good == 0:
        rowChoice = choices()
        colChoice = choices()
        if board[rowChoice-1][colChoice-1] == "x" or board[rowChoice-1][colChoice-1] == "o":
            print("The Place is Already Full !!")
        else:
            board[rowChoice-1][colChoice-1]=chance
            good = 1
            displayBoard(board)
    if turn >=5:
        return checkWin(rowChoice,colChoice,chance,board)
    else :
        return 0
def oTurn(board,turn):
    chance = "o"
    good = 0
    while good == 0:
        rowChoice = choices()
        colChoice = choices()
        if board[rowChoice-1][colChoice-1] == "x" or board[rowChoice-1][colChoice-1] == "o" :
            print("The Place is Already Full !!")
        else:
            board[rowChoice-1][colChoice-1]=chance
            good = 1
            displayBoard(board)
    if turn >=5:
        return checkWin(rowChoice,colChoice,chance,board)
    else :
        return 0
def checkDiagonals(board,chance):
    i=0
    j=2
    diag1=[]
    diag2=[]
    while i<=2:
        diag1.append(board[i][j])
        diag2.append(board[j][i])
        i+=1
        j-=1
    if "x" not in diag1 or "o" not in diag1:
        return 0
    if "x" not in diag2 or "o" not in diag2:
        return 0
    if len(set(diag1)) == 1 or len(set(diag2)) == 1:
        print(chance,"WINS!!!")
        return 1
    else:
        return 0

def checkWin(rowChoice,colChoice,chance,board):
    col=[]
    for i in board:
        col.append(i[colChoice-1])
    if len(set(board[rowChoice-1]))==1:
        print(chance,"WINS!!!")
        return 1
    elif len(set(col)) == 1:
        print(chance,"WINS!!!")
        return 1
    elif colChoice == 1 or colChoice == 3:
        return checkDiagonals(board,chance)
    else :
        return 0

def displayBoard(board):
    for i in board:
        for j in i:
            print(j,end="\t")
        print("\n")

winFlag = 0
turn = 1
displayBoard(board)
while winFlag == 0:
    print("TURN NO:",turn)
    if turn <=9:
        if turn%2 == 0:
            print("It's O's Turn Now !!")
            winFlag=oTurn(board,turn)
            turn+=1
        else :
            print("It's X's Turn Now !!")
            winFlag=xTurn(board,turn)
            turn+=1
    else:
        print("ITS A DRAW !!")