board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def getAvailables(funcBoard:list[list],cellX:int,cellY:int):
    available = [str(i) for i in range(1,10)]
    for row in range(len(funcBoard)):
        if funcBoard[row][cellY] in available:
                available.remove(funcBoard[row][cellY])
        if funcBoard[cellX][row] in available:
                available.remove(funcBoard[cellX][row])
    for i in range(cellX//3*3,cellX//3*3+3):
        for j in range(cellY//3*3,cellY//3*3+3):
            if funcBoard[i][j] in available:
                    available.remove(funcBoard[i][j])

    return available
            
# print(getAvailables(funcBoard,7,7))        

def Fill(funcBoard:list[list],cellX:int,cellY:int)->list[list]:
    ### getting available variants for every cell
    # print(cellX,":",cellY)
    res = []
    if funcBoard[cellX][cellY]==".":
        availables = getAvailables(funcBoard,cellX,cellY)
        if availables==[]:
            return
        else:
            for val in getAvailables(funcBoard,cellX,cellY):
                funcBoard[cellX][cellY]=val
                if cellX==8 and cellY==8:
                    funcBoard[cellX][cellY] = availables[0]
                    res = funcBoard
                else:
                    res =  Fill(funcBoard,cellX+(cellY+1)//9,(cellY+1)%9)
                    if res!=None:
                        return res
                    funcBoard[cellX][cellY]="."
    else:
        if cellX==8 and cellY==8:
            res =  funcBoard
        else:
            res = Fill(funcBoard,cellX+(cellY+1)//9,(cellY+1)%9)
    return res


res = Fill(board,0,0)
text = ""
for i in range(len(res)):
    if (i)%3==0:
        text+=f"{'-'*18}\n"
    for j in range(len(res[i])):
        text += f"{res[i][j]}"
        if (j+1)%3==0:
            text+="|"
        else:
            text+=" "
        if j==8:
            text+="\n"
            
print(text)