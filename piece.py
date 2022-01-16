from os.path import join
import pygame

def read_img(path):
    return pygame.image.load(join('img', path))

# white pieces
w_pawn = read_img('white_pawn.png')
w_rook = read_img('white_rook.png')
w_knight = read_img('white_knight.png')
w_bishop = read_img('white_bishop.png')
w_queen = read_img('white_queen.png')
w_king = read_img('white_king.png')

# black pieces
b_pawn = read_img('black_pawn.png')
b_rook = read_img('black_rook.png')
b_knight = read_img('black_knight.png')
b_bishop = read_img('black_bishop.png')
b_queen = read_img('black_queen.png')
b_king = read_img('black_king.png')

black_pieces = [b_pawn, b_rook, b_knight, b_bishop, b_queen, b_king]
white_pieces = [w_pawn, w_rook, w_knight, w_bishop, w_queen, w_king]

piece_size = 55

B = [pygame.transform.scale(img, (piece_size, piece_size)) for img in black_pieces]
W = [pygame.transform.scale(img, (piece_size, piece_size)) for img in white_pieces]



class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False


    def move(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, window):
        if self.color == 'w':
            drawThis = W[self.img]
        if self.color == 'b':
            drawThis = B[self.img]
        x = 5 + round(self.startX + (self.col * self.rect[2]/8))
        y = 5 + round(self.startY + (self.row * self.rect[2]/8))

        window.blit(drawThis, (x, y))



class Pawn(Piece):
    img = 0


class Rook(Piece):
    img = 1


class Knight(Piece):
    img = 2


class Bishop(Piece):
    img = 3


class Queen(Piece):
    img = 4


class King(Piece):
    img = 5
