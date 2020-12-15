import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = load_image('creature.png')
cursor.rect = cursor.image.get_rect()
all_sprites.draw(screen)

cursor.rect.x = 50
cursor.rect.y = 50

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and cursor.rect.x > 1:
            cursor.rect.x -= 10
        if keys[pygame.K_RIGHT] and cursor.rect.x < width - cursor.rect.width:
            cursor.rect.x += 10
        if keys[pygame.K_UP] and cursor.rect.y > 1:
            cursor.rect.y -= 10
        if keys[pygame.K_DOWN] and cursor.rect.y < height - cursor.rect.height:
            cursor.rect.y += 10
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
