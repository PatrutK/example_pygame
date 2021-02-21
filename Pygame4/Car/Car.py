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


class Car(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('car.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 300
        self.speed = 5

    def update(self):
        if self.rect.x + self.rect.width > width:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed
        elif self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = - self.speed
        self.rect.x = self.rect.x + self.speed
        return self.speed


size = width, height = (600, 600)
clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
car = Car()
all_sprites.add(car)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for sprite in all_sprites:
        v = car.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
