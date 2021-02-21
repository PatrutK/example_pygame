import pygame


pygame.init()
size = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('К щелчку')

running = True
move = False

x, y = 400, 400
x_pos, y_pos = x, y
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move = True
            x_pos, y_pos = event.pos[0], event.pos[1]
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, pygame.color.Color('red'), (x, y), 20)

    if x_pos > x:
        x += 1
    elif x_pos < x:
        x -= 1
    if y_pos > y:
        y += 1
    elif y_pos < y:
        y -= 1

    clock.tick(60)
    pygame.display.flip()
pygame.quit()