import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

player = pygame.Rect(100, 500, 60, 80)

coins = []
coin_size = 1

speed = 5

score = 0
font = pygame.font.SysFont(None, 20)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    player.x = max(0, min(WIDTH - player.width, player.x))

    if random.randint(1, 25) == 1:
        coin = pygame.Rect(random.randint(0, WIDTH - coin_size), 0, coin_size, coin_size)
        coins.append(coin)

    for coin in coins:
        coin.y += speed

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    pygame.draw.rect(screen, BLACK, player)

    for coin in coins:
        pygame.draw.rect(screen, YELLOW, coin)

    text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(text, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

