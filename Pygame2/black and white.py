import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        color = pygame.Color(255, 255, 255)
        for j in range(self.height):
            for i in range(self.width):
                if self.board[j][i] == 0:
                    width = 1
                else:
                    width = 0
                pygame.draw.rect(screen, color, (
                    self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size,
                    self.cell_size), width)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if (0 <= cell_x < self.width) and (0 <= cell_y < self.height):
            return (cell_x, cell_y)
        else:
            return None

    def on_click(self, cell_coords):
        if cell_coords:
            for i in range(self.height):
                for j in range(self.width):
                    if i == cell_coords[1] or j == cell_coords[0]:
                        if self.board[i][j] == 0:
                            self.board[i][j] = 1
                        else:
                            self.board[i][j] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
size = 570, 570
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Чёрное в белое и наоборот')
board = Board(11, 11)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
