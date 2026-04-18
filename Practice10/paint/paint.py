import pygame

pygame.init()

WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

drawing = False
mode = "pen"
color = (0, 0, 0)
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_1:
                color = (0, 255, 0)
            if event.key == pygame.K_2:
                color = (0, 0, 255)
            if event.key == pygame.K_3:
                color = (255, 0, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "rect":
                pygame.draw.rect(screen, color, (*start_pos, end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) **2 + (end_pos[1] - start_pos[1]) **2) **0.5)
                pygame.draw.circle(screen, color, start_pos, radius)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.circle(screen, color, event.pos, 5)
            elif mode == "eraser":
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 15)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
                