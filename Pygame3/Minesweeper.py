import pygame
from random import randint


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
        mine_color = pygame.Color('red')
        for j in range(self.height):
            for i in range(self.width):
                if self.board[j][i] == 0:
                    color = pygame.Color('black')
                    for x in range(len(self.board)):
                        if self.rand[x] % 3 == 0:
                            pygame.draw.rect(screen, mine_color, (
                                self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size,
                                self.cell_size), 0)

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
            x, y = cell_coords
            self.board[y][x] = (self.board[y][x] + 1) % 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def random_cell(self):
        self.rand = [randint(0, 10) for i in range(len(self.board))]
        board_list = [(randint(0, 2), randint(0, 2)) for i in range(len(self.board))]
        print(board_list)


class Minesweeper(Board):
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height)
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        if cell:
            x, y = cell
            super().on_click(cell)
            print(self.count_life_cell(x, y))

    def count_life_cell(self, x, y):
        count = 0
        delta = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0) or (dy != 0)]
        for dx, dy in delta:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                if self.board[y + dy][x + dx] == 1:
                    count += 1
        return count

    def next_move(self):
        pass


pygame.init()
size = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Дед Сапёра')
board1 = Minesweeper(30, 30, 10, 10, 19)
board = Board(30, 30)
board1.count_life_cell(2, 4)
running = True
board1.random_cell()
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
