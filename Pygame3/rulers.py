import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['.'] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50
        self.player = True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for j in range(self.height):
            for i in range(self.width):
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
        print(cell)
        self.on_click(cell)


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def on_click(self, cell):
        if cell:
            x, y = cell
            if self.board[y][x] != 'b':
                self.board[y][x] = 'b'
            else:
                self.board[y][x] = 'r'

    def open_cell(self, cell):
        if cell:
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
        colors = {'r': 'red', 'b': 'blue'}
        for j in range(self.height):
            for i in range(self.width):
                if self.board[j][i] in colors:
                    color = colors[self.board[j][i]]
                else:
                    color = 'black'
                pygame.draw.ellipse(screen, color, (
                    self.left + i * self.cell_size + 4, self.top + j * self.cell_size + 4, self.cell_size - 8,
                    self.cell_size - 8), 0)
        super().render(screen)


pygame.init()
size = 470, 470
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Линеечки')
board = Lines(9, 9)
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
