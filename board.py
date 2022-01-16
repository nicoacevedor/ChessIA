from piece import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self, color = 'w'):
        self.rows = 8
        self.cols = 8
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.players = ('w', 'b')

        if color == 'b':
            self.players = ('b', 'w')

        self.board[0][0] = Rook(0, 0, self.players[1])
        self.board[0][1] = Knight(0, 1, self.players[1])
        self.board[0][2] = Bishop(0, 2, self.players[1])
        self.board[0][3] = Queen(0, 3, self.players[1])
        self.board[0][4] = King(0, 4, self.players[1])
        self.board[0][5] = Bishop(0, 5, self.players[1])
        self.board[0][6] = Knight(0, 6, self.players[1])
        self.board[0][7] = Rook(0, 7, self.players[1])
        self.board[1] = [Pawn(1, k, self.players[1]) for k in range(8)]

        self.board[7][0] = Rook(7, 0, self.players[0])
        self.board[7][1] = Knight(7, 1, self.players[0])
        self.board[7][2] = Bishop(7, 2, self.players[0])
        self.board[7][3] = Queen(7, 3, self.players[0])
        self.board[7][4] = King(7, 4, self.players[0])
        self.board[7][5] = Bishop(7, 5, self.players[0])
        self.board[7][6] = Knight(7, 6, self.players[0])
        self.board[7][7] = Rook(7, 7, self.players[0])
        self.board[6] = [Pawn(6, k, self.players[0]) for k in range(8)]


    def draw(self, window):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(window)
