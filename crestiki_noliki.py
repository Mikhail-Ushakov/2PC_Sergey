from tkinter import *

# Const
CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

# Player steup
X = 'player 1'
O = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.game_status = True
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            ]

    def minimax(self,board, isMax):
        board_len = range(len(self.board))

        if self.check_win(board, O):
            return 1
        elif self.check_win(board, X):
            return -1
        elif self.check_draw(board):
            return 0
        # print(board)
        if isMax:
            best_score = float('-inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = O
                        self.change_player() 
                        score = self.minimax(board, False)
                        board[i][j] = EMPTY
                        best_score = max(score,best_score)
        else:
            best_score = float('inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = X
                        self.change_player() 
                        score = self.minimax(board, True)
                        board[i][j] = EMPTY
                        best_score = min(score,best_score)
        return best_score

    def click_event(self, pos):
        x_coord = pos.x // FIGURE_SIZE
        y_coord = pos.y // FIGURE_SIZE
        self.make_move(x_coord, y_coord)

        if self.game_status:
            self.ai_best_move()

    def ai_best_move(self):
        best_score = float('-inf')
        board_len = range(len(self.board))
        board = self.board[:]
        for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = O
                        score = self.minimax(board, False)
                        print('score =', score)
                        print('bscore =', best_score)
                        board[i][j] = EMPTY
                        if score > best_score:
                            best_score = score
                            move = i, j
        self.make_move(move[0], move[1])
        
    def make_move(self, x, y):
        if self.board[x][y] == EMPTY:            
            if self.current_player == X:
                self.render_cross(x*FIGURE_SIZE, y*FIGURE_SIZE)
            else:
                self.render_circle(x*FIGURE_SIZE, y*FIGURE_SIZE)
            self.board[x][y]=self.current_player

            if self.check_win(self.board, self.current_player):
                self.winner(self.current_player)
            elif self.check_draw(self.board):
                self.winner()
            
            self.change_player() 
            print(self.board)
        else:
            print('Клетка занята, попробуйте другую')
            self.canvas.bind('<Button-1>', self.click_event)

        
        
            
    def change_player(self):
        if self.current_player == X:
            self.current_player = O
        else:
            self.current_player = X

    def check_draw(self, board):
        for i in board:
            if EMPTY in i:
                return False
        return True

    def check_win(self, board, c_player):
        for y in range(3):
            if board[y][0] == board[y][1] == board[y][2] == c_player:
                return True
        for x in range(3):
            if board[0][x] == board[1][x] == board[2][x] == c_player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == c_player:
            return True
        elif board[0][2] == board[1][1] == board[2][0] == c_player:
            return True
        return False

    def build_grid(self,grid_color):
        x = 200
        y = 600
        for i in range(2):
            self.canvas.create_line(x, 0, x, y, fill=grid_color)
            self.canvas.create_line(0, x, y, x, fill=grid_color)
            x += 200
        
    def render_cross(self,posX,posY):
        self.canvas.create_line(posX, posY, posX + FIGURE_SIZE, posY + FIGURE_SIZE, fill='red', width = 5)
        self.canvas.create_line(posX + FIGURE_SIZE, posY, posX, posY + FIGURE_SIZE, fill='red', width = 5)

    def render_circle(self,posX,posY):
        self.canvas.create_oval(posX + 5,posY + 5,posX + FIGURE_SIZE - 5, posY + FIGURE_SIZE - 5, outline = 'blue', width = 5)

    def winner(self,player=None):
        game_status = False
        center = CANVAS_SIZE // 2
        if player:
            text = f'winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text=text, fill='white', font='Arial 50')
        self.canvas.unbind('<Button-1>')

game_v1 = Board(start_player = FIRST_PLAYER)
game_v1.build_grid('white')
game_v1.title('Tic Tac Toe')

game_v1.mainloop()