import pygame
import sys
from datetime import datetime
from tools import flood_fill
import math

pygame.init()

WIDTH, HEIGHT = 900, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint++")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

color = (0, 0, 0)
brush_size = 5
tool = "pencil"

drawing = False
start_pos = None
last_pos = None

font = pygame.font.SysFont(None, 30)
typing = False
text = ""
text_pos = (0, 0)

def draw_rectangle(surface, color, start, end, w):
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, w)

def draw_square(surface, color, start, end, w):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], side, side)
    pygame.draw.rect(surface, color, rect, w)

def draw_circle(surface, color, start, end, w):
    r = int(math.hypot(end[0] - start[0], end[1] - start[1]))
    pygame.draw.circle(surface, color, start, r, w)

def draw_right_triangle(surface, color, start, end, w):
    points = [start, end, (start[0],end[1])]
    pygame.draw.polygon(surface, color, points, w)

def draw_equilateral_triangle(surface, color, start, end, w):
    side = abs(end[0] - start[0])
    h = int((3**0.5/2)*side)
    p1 = start
    p2 = (start[0] + side, start[1])
    p3 = (start[0] + side // 2, start[1] - h)
    pygame.draw.polygon(surface, color, [p1, p2, p3], w)

def draw_rhombus(surface, color, start, end, w):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2
    pts = [(cx, start[1]), (end[0], cy), (cx, end[1]), (start[0], cy)]
    pygame.draw.polygon(surface, color, pts, w)    


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = 5
            elif event.key == pygame.K_2:
                brush_size = 7
            elif event.key == pygame.K_3:
                brush_size = 10

            elif event.key == pygame.K_p:
                tool = "pencil"
            elif event.key == pygame.K_l:
                tool = "line"
            elif event.key == pygame.K_f:
                tool = "fill"
            elif event.key == pygame.K_t:
                tool = "text"

            elif event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_q:
                tool = "square"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_a:
                tool = "right_triangle"
            elif event.key == pygame.K_e:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"

            
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("canvas_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)

            if typing:
                if event.key == pygame.K_RETURN:
                    img = font.render(text, True, color)
                    canvas.blit(img, text_pos)
                    typing = False
                    text = ""
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode   

        if event.type == pygame.MOUSEBUTTONDOWN:

            if tool == "fill":
                flood_fill(canvas, *event.pos, color)

            elif tool == "text":
                typing = True
                text_pos = event.pos
                text = ""  

            else:
                drawing = True
                start_pos = event.pos  
                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if start_pos:
                if tool == "line":
                    pygame.draw.line(canvas, color, start_pos, event.pos, brush_size)

                elif tool == "rectangle":
                    draw_rectangle(canvas, color, start_pos, event.pos, brush_size)

                elif tool == "square":
                    draw_square(canvas, color, start_pos, event.pos, brush_size)

                elif tool == "circle":
                    draw_circle(canvas, color, start_pos, event.pos, brush_size)

                elif tool == "right_triangle":
                    draw_right_triangle(canvas, color, start_pos, event.pos, brush_size)

                elif tool == "equilateral_triangle":
                    draw_equilateral_triangle(canvas, color, start_pos, event.pos, brush_size)

                elif tool == "rhombus":
                    draw_rhombus(canvas, color, start_pos, event.pos, brush_size)

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos


    screen.blit(canvas, (0, 0))

    if drawing and start_pos and tool != "pencil":
        temp = canvas.copy()
        mouse = pygame.mouse.get_pos()

        if tool == "line":
            pygame.draw.line(temp, color, start_pos, mouse, brush_size)
        elif tool == "rectangle":
            draw_rectangle(temp, color, start_pos, mouse, brush_size)
        elif tool == "square":
            draw_square(temp, color, start_pos, mouse, brush_size)
        elif tool == "circle":
            draw_circle(temp, color, start_pos, mouse, brush_size)
        elif tool == "right_triangle":
            draw_right_triangle(temp, color, start_pos, mouse, brush_size)
        elif tool == "equilateral_triangle":
            draw_equilateral_triangle(temp, color, start_pos, mouse, brush_size)
        elif tool == "rhombus":
            draw_rhombus(temp, color, start_pos, mouse, brush_size) 

        screen.blit(temp, (0, 0))

    if typing:
        img = font.render(text, True, color)
        screen.blit(img, text_pos)

    pygame.display.flip()
    clock.tick(60)
