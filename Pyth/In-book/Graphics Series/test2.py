square.grid("<Button-1>", on_click)

def on_click(event):
    global score
    global gameOver
    global squaresToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver == False:
        if bombfield[row][column] == 1:
            gameOver = True
            square.config(bg = "red")
            print("Trò chơi kết thúc! Bạn giẫm phỉa bom!")
            print("Số điểm của bạn là:", score)
        elif currentText == "  ":
            square.config(bg = "brown")
            totalBombs = 0
            if row < 9:
                if bombfield[row+1][column] == 1:
                    totalBombs = totalBombs + 1
            if row > 0:
                if bombfield[row-1][column] == 1:
                    totalBombs = totalBombs + 1
            if column > 0:
                if bombfield[row][column-1] == 1:
                    totalBombs = totalBombs + 1
            if column < 9:
                if bombfield[row][column+1] == 1:
                    totalBombs = totalBombs + 1
            if row > 0 and column > 0:
                if bombfield[row-1][column-1] == 1:
                    totalBombs = totalBombs + 1
            if row < 9 and column > 0:
                if bombfield[row+1][column-1] == 1:
                    totalBombs = totalBombs + 1
play_bombdodger()