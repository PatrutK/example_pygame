import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Двигающийся куб')
    running = True
    font = pygame.font.Font(None, 72)
    n = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEOEXPOSE:
                n += 1
        text = font.render("{}".format(n), True, (255, 0, 0))
        place = text.get_rect(
            center=(100, 100))
        screen.blit(text, place)
        pygame.display.flip()
        screen.fill((0, 0, 0))
pygame.quit()
