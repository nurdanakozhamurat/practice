import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x = WIDTH // 2
y = HEIGHT // 2
move_step = 20

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x - move_step - radius >= 0:
                    x -= move_step

            elif event.key == pygame.K_RIGHT:
                if x + move_step + radius <= WIDTH:
                    x += move_step

            elif event.key == pygame.K_UP:
                if y - move_step - radius >= 0:
                    y -= move_step

            elif event.key == pygame.K_DOWN:
                if y + move_step + radius <= HEIGHT:
                    y += move_step

    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()