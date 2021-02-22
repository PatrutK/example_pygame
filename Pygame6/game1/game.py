import pygame
import sys
import os

size = width, height = (900, 900)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)


def terminate():
    pygame.quit()
    sys.exit()


def load_level(name):
    fullname = "data/" + name
    with open(fullname, 'r') as map_file:
        level_map = []
        for line in map_file:
            line = line.strip()
            level_map.append(line)
    return level_map


def draw_level(level_map):
    new_player, x, y = None, None, None
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == '.':
                Tile('grass.png', x, y)
            elif level_map[y][x] == '#':
                Tile('box.png', x, y)
            elif level_map[y][x] == '@':
                Tile('grass.png', x, y)
                new_player = Player(x, y)
    return new_player, x, y


tile_width = tile_height = 50
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image(tile_type)
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

        if tile_type == 'box.png':
            self.add(box_group, tiles_group, all_sprites)
        else:
            self.add(tiles_group, all_sprites)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = load_image('mario.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(50 * pos_x, 50 * pos_y)

        self.add(player_group, all_sprites)

    def move_up(self):
        self.rect = self.rect.move(0, -50)

    def move_down(self):
        self.rect = self.rect.move(0, +50)

    def move_left(self):
        self.rect = self.rect.move(-50, 0)

    def move_right(self):
        self.rect = self.rect.move(+50, 0)


class Camera:
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size

    def apply(self, obj):
        obj.rect.x += self.dx

        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * obj.rect.width

        if obj.rect.x >= (self.field_size[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
        obj.rect.y += self.dy

        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * obj.rect.height
        if obj.rect.y >= (self.field_size[1]) * obj.rect.height:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()

player, level_x, level_y = draw_level(load_level("map.txt"))
camera = Camera((level_x, level_y))
start_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.move_up()
            if pygame.sprite.spritecollideany(player, box_group):
                player.move_down()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player.move_down()
            if pygame.sprite.spritecollideany(player, box_group):
                player.move_up()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.move_left()
            if pygame.sprite.spritecollideany(player, box_group):
                player.move_right()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.move_right()
            if pygame.sprite.spritecollideany(player, box_group):
                player.move_left()

        if event.type == pygame.QUIT:
            terminate()

    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)

    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

terminate()
