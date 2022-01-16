import pygame
from os.path import join
from board import Board


board = pygame.image.load(join('img', 'board_alt.png'))

width, height = 750, 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("ChessIA Game")

def redraw_window():
    global window
    window.blit(pygame.transform.scale(board, (width, height)), (0, 0))
    b = Board()
    b.draw(window)

    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


if __name__ == '__main__':
    main()
