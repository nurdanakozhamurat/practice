import pygame
from collections import deque

def flood_fill(surface, start_x, start_y, new_color):
    width, height = surface.get_size()

    original_color = surface.get_at((start_x, start_y))

    if original_color == new_color:
        return

    pixels_queue = deque()
    pixels_queue.append((start_x, start_y))

    while pixels_queue:
        current_x, current_y = pixels_queue.popleft()


        if current_x < 0 or current_x >= width:
            continue
        if current_y < 0 or current_y >= height:
            continue

        current_color = surface.get_at((current_x, current_y))

        if current_color != original_color:
            continue


        surface.set_at((current_x, current_y), new_color)

        pixels_queue.append((current_x+1, current_y))
        pixels_queue.append((current_x-1, current_y))
        pixels_queue.append((current_x, current_y+1))
        pixels_queue.append((current_x, current_y-1))