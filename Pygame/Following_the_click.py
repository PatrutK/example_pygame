import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Следование за шариком')

    running = True
    move = False

    color = pygame.Color('red')
    radius = 20
    clock = pygame.time.Clock()
    x_pos = width / 2
    y_pos = height / 2
    v = 10
    x, y = 0, 0
    dx, dy = 0, 0

    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                move = True
        # отрисовка и изменение свойств объектов
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), radius)
        # pygame.draw.line(screen, (255, 0, 0), (0, height / 2), (width, height / 2), width=1)
        if move:
            dx = x_pos - x
            dy = y_pos - y
            # print(x_pos, x)
            # move = False
            if x_pos > x:
                x_pos -= v * clock.tick() / 100  # v * t в секундах
            elif x_pos < x:
                x_pos += v * clock.tick() / 100  # v * t в секундах
        # обновление экрана
        pygame.display.flip()
    pygame.quit()
