import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Перетаскивание')

    clock = pygame.time.Clock()
    running = True
    rect_x = rect_y = 25
    rect_size = 50
    rect_color = pygame.Color('green')
    drag = False
    isJump = False
    jumpCount = 10
    v = 1

    while running:
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
        # else:
        #     if jumpCount >= -10:
        #         if jumpCount < 0:
        #             print(jumpCount)
        #             rect_y += (jumpCount * 2) / 2
        #         else:
        #             rect_y -= (jumpCount * 2) / 2
        #         jumpCount -= 1
        #     else:
        #         isJump = False
        #         jumpCount = 10

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_size, rect_size))
        pygame.display.flip()
    pygame.quit()