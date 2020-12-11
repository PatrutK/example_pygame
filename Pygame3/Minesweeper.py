import pygame
from random import randint


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        print(self.board)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, pos):
        cell_x = (pos[0] - self.left) // self.cell_size
        cell_y = (pos[1] - self.top) // self.cell_size
        if (0 <= cell_x < self.width) and (0 <= cell_y < self.height):
            return (cell_x, cell_y)

    def on_click(self, cell):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen, pygame.Color('green'), (
                        self.left + x * self.cell_size, self.top + self.cell_size * y,
                        self.cell_size,
                        self.cell_size))

                pygame.draw.rect(screen, pygame.Color('white'), (
                    self.left + x * self.cell_size, self.top + self.cell_size * y, self.cell_size,
                    self.cell_size), 1)


class Minesweeper(Board):
    def __init__(self, width, height, mines=10):
        super().__init__(width, height)
        self.left = 10
        self.top = 10
        self.cell_size = 50
        self.mines = mines
        count = 0
        while True:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if self.board[y][x] == (-1):
                self.board[y][x] = 10
                count += 1
            if count == self.mines:
                break

    def on_click(self, cell):
        self.open_cell(cell)

    def open_cell(self, cell):
        x, y = cell
        self.board[y][x] = self.count_mines_for_cell(x, y)

    def count_mines_for_cell(self, x, y):
        count = 0
        delta = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0) or (dy != 0)]
        for dx, dy in delta:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                if self.board[y + dy][x + dx] == 10:
                    count += 1
        return count

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, pygame.Color('red'), (
                        self.left + x * self.cell_size, self.top + self.cell_size * y,
                        self.cell_size,
                        self.cell_size))
                elif self.board[y][x] != -1:
                    font = pygame.font.Font(None, self.cell_size)
                    text = font.render(str(self.board[y][x]), True, (0, 255, 0))
                    screen.blit(text, (self.left + x * self.cell_size + 2, self.top + y * self.cell_size + 2))

                pygame.draw.rect(screen, pygame.Color('white'), (
                    self.left + x * self.cell_size, self.top + self.cell_size * y, self.cell_size,
                    self.cell_size), 1)


if __name__ == '__main__':
    pygame.init()
    size = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Прадедушка сапера')

    board = Minesweeper(10, 10, 50)
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
