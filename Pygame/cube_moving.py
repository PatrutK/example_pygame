import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Двигающийся куб')
    clock = pygame.time.Clock()

    rect_x, rect_y = 25, 800 - 50
    rect_size = 50
    jumpCount = 10
    v = 5
    isJump = False
    running = True

    while running:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rect_x > 1:
            rect_x -= v
        if keys[pygame.K_RIGHT] and rect_x < width - rect_size:
            rect_x += v
        if not isJump:
            if keys[pygame.K_UP] and rect_y > 1:
                rect_y -= v
            if keys[pygame.K_DOWN] and rect_y < height - rect_size:
                rect_y += v
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    rect_y += (jumpCount ** 2) / 2
                else:
                    rect_y -= (jumpCount ** 2) / 2
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_size, rect_size))
        pygame.display.flip()
    pygame.quit()
