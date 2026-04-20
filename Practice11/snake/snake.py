import pygame
import random
import time

pygame.init()

width, height = 600, 600
cell = 10
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake+")

clock = pygame.time.Clock()

snake = [(500, 300)]
direc = (cell, 0)

def gen_food():
    x = random.randrange(0, width, cell)
    y = random.randrange(0, height, cell)
    weight = random.choice([1, 2, 3])
    gen_time = time.time()
    return {"pos":(x,y), "weight":weight, "time":gen_time}

food = gen_food()

score = 0
speed = 6

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

    head = (snake[0][0]+direc[0], snake[0][1]+direc[1])
    snake.insert(0, head)

    if food == food["pos"]:
        score += food["weight"]
        food = gen_food()
    else:
        snake.pop()

    if time.time() - food["time"] > 6:
        food = gen_food()

    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, cell, cell))

    if food["weight"] == 1:
        color = (255, 0, 0)
    elif food["weight"] == 2:
        color = (255, 255, 255)
    else:
        color = (0, 0, 255)
    pygame.draw.rect(screen, color, (*food["pos"], cell, cell))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
