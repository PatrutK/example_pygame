import pygame
from random import randint

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шарики')

    running = True

    color = pygame.Color('white')
    radius = 10
    clock = pygame.time.Clock()
    circles = []

    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                circles.append([event.pos[0], event.pos[1], -1, -1])

        # отрисовка и изменение свойств объектов
        screen.fill((0, 0, 0))
        for i in range(len(circles)):
            x_pos, y_pos, dx, dy = circles[i]
            circles[i][0] = max(circles[i][0], radius)
            circles[i][0] = min(circles[i][0], width - radius)
            circles[i][1] = max(circles[i][1], radius)
            circles[i][1] = min(circles[i][1], height - radius)

            if not (radius <= x_pos <= width - radius):
                color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
                circles[i][2] = -circles[i][2]
            if not (radius <= y_pos <= height - radius):
                color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
                circles[i][3] = -circles[i][3]
            circles[i][0] += circles[i][2]
            circles[i][1] += circles[i][3]

            pygame.draw.circle(screen, color, (max(x_pos, radius), max(y_pos, radius)), radius)
        clock.tick(100)
        # обновление экрана
        pygame.display.flip()
    pygame.quit()
