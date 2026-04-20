import pygame
import math

pygame.init()

width, height = (600, 400)
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))

mode = "pen"
color = (0,0,0)
drawing = False
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s: mode = "square"
            if event.key == pygame.K_t: mode = "triangle"
            if event.key == pygame.K_e: mode = "eq_triangle"
            if event.key == pygame.K_r: mode = "rhombus"
            if event.key == pygame.K_p: mode = "pen"

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            x1,y1 = start_pos
            x2,y2 = end_pos

            if mode == "square":
                side = min(abs(x2-x1), abs(y2-y1))
                pygame.draw.rect(screen, color, (x1,y1,side,side))

            elif mode == "triangle":
                pygame.draw.polygon(screen, color, [(x1,y1),(x2,y2),(x1,y2)])

            elif mode == "eq_triangle":
                side = abs(x2-x1)
                height = side * math.sqrt(3)/2
                pygame.draw.polygon(screen, color, [
                    (x1,y1),
                    (x1+side,y1),
                    (x1+side/2, y1-height)
                ])

            elif mode == "rhombus":
                mx = (x1+x2)//2
                my = (y1+y2)//2
                pygame.draw.polygon(screen, color, [
                    (mx,y1),
                    (x2,my),
                    (mx,y2),
                    (x1,my)
                ])

        if event.type == pygame.MOUSEMOTION and drawing and mode=="pen":
            pygame.draw.circle(screen, color, event.pos, 3)

    pygame.display.flip()

pygame.quit()