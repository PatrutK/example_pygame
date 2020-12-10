import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.player = 'x'
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
        x, y = cell
        self.board[y][x] = (self.board[y][x] + 1) % 2

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


class Live(Board):
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height)
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.pause = True

    def on_click(self, cell):
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
        new_board = [[0] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if (self.board[y][x] == 0) and (self.count_life_cell(x, y) == 3):
                    new_board[y][x] = 1
                if self.board[y][x] == 1:
                    if 2 <= self.count_life_cell(x, y) <= 3:
                        new_board[y][x] = 1
                    else:
                        new_board[y][x] = 0
        self.board = new_board


if __name__ == '__main__':
    size_cell = 20
    otstup = 10
    cell_count = 40
    pygame.init()
    size = size_cell * cell_count + otstup * 2, size_cell * cell_count + otstup * 2
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра в жизнь')

    board = Live(cell_count, cell_count, otstup, otstup, size_cell)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    board.pause = not board.pause
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        if not (board.pause):
            board.next_move()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
