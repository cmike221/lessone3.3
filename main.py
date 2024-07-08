import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Скрин1.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 108
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счетчик успешных попаданий
score = 0
font = pygame.font.Font(None, 36)

# Установить таймер для перемещения цели
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 1000)

running = True
while running:
    screen.fill(colour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y + 28 < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if event.type == MOVE_EVENT:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.blit(target_img, (target_x, target_y))

    # Отображение счетчика на экране
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
