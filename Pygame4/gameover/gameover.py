import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


size = width, height = (600, 300)
clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode(size)

game_over = pygame.sprite.Sprite()
game_over.image = load_image("gameover.png")
all_sprites = pygame.sprite.Group()
all_sprites.add(game_over)

game_over.rect = game_over.image.get_rect()
game_over.rect.x = -600
game_over.rect.y = 0

running = True
run = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if run:
        game_over.rect.x += 10
        if game_over.rect.width + game_over.rect.x == width:
            run = False
    screen.fill((0, 0, 0))
    clock.tick(fps)
    all_sprites.draw(screen)
    pygame.display.flip()
