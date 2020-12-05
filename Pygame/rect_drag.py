import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Перетаскивание')

    clock = pygame.time.Clock()
    running = True
    rect_x = rect_y = 0
    rect_size = 100
    rect_color = pygame.Color('green')
    drag = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                drag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (rect_x <= x <= rect_x + rect_size) and (rect_y <= y <= rect_y + rect_size):
                    drag = True
                    dx = x - rect_x
                    dy = y - rect_y
            if event.type == pygame.MOUSEMOTION:
                if drag:
                    rect_x = event.pos[0] - dx
                    rect_y = event.pos[1] - dy

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_size, rect_size))
        pygame.display.flip()
    pygame.quit()




