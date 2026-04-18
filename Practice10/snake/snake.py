import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
cell = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake = [(100, 100)]
direc = (cell, 0)

def food():
    while True:
        x=random.randrange(0, WIDTH, cell)
        y=random.randrange(0, HEIGHT, cell)
        if (x, y) not in snake:
            return (x, y)

f = food()
score = 0
level = 1
speed = 3

font = pygame.font.SysFont(None, 20)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direc = (0, -cell)
    if keys[pygame.K_DOWN]:
        direc = (0, cell)
    if keys[pygame.K_LEFT]:
        direc = (-cell, 0)
    if keys[pygame.K_RIGHT]:
        direc = (cell, 0)

    head = (snake[0][0] + direc[0], snake[0][1] + direc[1])

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    if head in snake:
        running = False
    
    snake.insert(0, head)

    if head == f:
        score += 1
        f = food()

        if score % 2 ==0:
            level += 1
            speed +=2
    else:
        snake.pop()

    for s in snake:
        pygame.draw.rect(screen, (0, 0, 255), (*s, cell, cell))

    pygame.draw.rect(screen, (0, 255, 0), (*f, cell, cell))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))

    screen.blit(score_text, (10, 20))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()

