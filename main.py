import pygame
import sys
import random

# Инициализируем pygame
pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Устанавливаем заголовок окна
pygame.display.set_caption("Подземелье")

# Цвета
black = (0, 0, 0)

# Загрузка изображений
player_img = pygame.image.load('pngwing.com.png')  # Замените на ваше изображение персонажа
monster_img = pygame.image.load('pngwing.com.png')  # Замените на ваше изображение монстра

# Позиции и размеры
player_size = player_img.get_size()
player_position = [screen_width / 2 - player_size[0] / 2, screen_height - player_size[1]]
monster_size = monster_img.get_size()
monster_position = [screen_width / 2 - monster_size[0] / 2, 50]

# Скорость
player_speed = 0.3

# Функция для проверки попадания
def is_hit(player_pos, monster_pos, player_size, monster_size):
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size[0], player_size[1])
    monster_rect = pygame.Rect(monster_pos[0], monster_pos[1], monster_size[0], monster_size[1])
    return player_rect.colliderect(monster_rect)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливаем экран черным цветом
    screen.fill(black)

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_position[0] += player_speed
    if keys[pygame.K_UP]:
        player_position[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_position[1] += player_speed
    if keys[pygame.K_SPACE]:
        if is_hit(player_position, monster_position, player_size, monster_size):
            monster_position = [random.randint(0, screen_width - monster_size[0]), random.randint(0, screen_height - monster_size[1])]

    # Ограничение движения персонажа в рамках экрана
    player_position[0] = max(player_position[0], 0)
    player_position[0] = min(player_position[0], screen_width - player_size[0])
    player_position[1] = max(player_position[1], 0)
    player_position[1] = min(player_position[1], screen_height - player_size[1])

    # Отрисовка персонажа и монстра
    screen.blit(player_img, player_position)
    screen.blit(monster_img, monster_position)

    # Обновляем экран
    pygame.display.flip()

# Выходим из pygame
pygame.quit()
sys.exit()
