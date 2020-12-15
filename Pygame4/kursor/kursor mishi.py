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
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()

cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = load_image('arrow.png')
cursor.rect = cursor.image.get_rect()
all_sprites.draw(screen)
running = True
pygame.mouse.set_visible(False)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            cursor.rect.x = x
            cursor.rect.y = y
    screen.fill((0, 0, 0))
    if pygame.mouse.get_focused():
        all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
