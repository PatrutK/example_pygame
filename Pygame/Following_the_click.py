import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шарики')

    running = True

    color = pygame.Color('red')
    radius = 20
    clock = pygame.time.Clock()
    c_x = width / 2
    c_y = height / 2

    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

        # отрисовка и изменение свойств объектов
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, color, (c_x, c_y), radius)

        clock.tick(100)
        # обновление экрана
        pygame.display.flip()
    pygame.quit()
