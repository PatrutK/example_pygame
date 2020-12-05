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
        color = pygame.Color('black')
        for j in range(self.height):
            for i in range(self.width):
                if self.board[j][i] == 0:
                    color = pygame.Color('black')
                elif self.board[j][i] == 1:
                    color = pygame.Color('red')
                else:
                    color = pygame.Color('blue')

                pygame.draw.rect(screen, color, (
                    self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size,
                    self.cell_size), 0)
                pygame.draw.rect(screen, (255, 255, 255), (
                    self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size,
                    self.cell_size), 1)

    def get_cell(self, mouse_pos):
        self.cell_x = (mouse_pos[0] - self.left) // self.cell_size
        self.cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if (0 <= self.cell_x < self.width) and (0 <= self.cell_y < self.height):
            return self.cell_x, self.cell_y
        else:
            return None

    def on_click(self, cell_coords):
        if cell_coords:
            print(self.board[self.cell_y][self.cell_x] + 1)
            self.board[self.cell_y][self.cell_x] = (self.board[self.cell_y][self.cell_x] + 1) % 3

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
size = 270, 370
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Реакции на мышку')
board = Board(5, 7)
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
