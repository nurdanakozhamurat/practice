import pygame
import random

pygame.init()

width, height = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer+")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

player = pygame.Rect(200, 150, 60, 40)
enemy = pygame.Rect(200, 0, 60, 40)

coins = []
score = 0
en_speed = 6

font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()

def gen_coins():
    weight = random.choice([1,2,3])
    size = weight*10
    x = random.randint(0, width - size)
    coin = pygame.Rect(x, 0, size, size)
    return coin, weight

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 6
    if keys[pygame.K_RIGHT]:
        player.x += 6

    player.x = max(0, min(width - player.width, player.x))

    if random.randint(1, 20) == 1:
        coins.append(gen_coins())

    enemy.y += en_speed
    if enemy.y > height:
        enemy.y = 0
        enemy.x = random.randint(0, width - enemy.width)

    for coin, w in coins:
        coin.y += 6

    for coin, w in coins[:]:
        if player.colliderect(coin):
            coins.remove((coin, w))
            score += w

            if score % 6 == 0:
                en_speed += 1

    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, RED, enemy)

    for coin, w in coins:
        if w == 1:
            color = (255, 255, 0)
        elif w == 2:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)
        pygame.draw.rect(screen, color, coin)

    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()