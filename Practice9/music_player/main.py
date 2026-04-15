import pygame
import sys
import os
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player with Keyboard Controller")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 200)

font_title = pygame.font.SysFont("Arial", 36)
font_text = pygame.font.SysFont("Arial", 28)
font_small = pygame.font.SysFont("Arial", 22)

music_folder = os.path.join(os.path.dirname(__file__), "music")
player = MusicPlayer(music_folder)

clock = pygame.time.Clock()


def draw_ui():
    screen.fill(WHITE)

    title = font_title.render("Pygame Music Player", True, BLUE)
    screen.blit(title, (230, 40))

    track_text = font_text.render(
        f"Current Track: {player.get_current_track_name()}",
        True,
        BLACK
    )
    screen.blit(track_text, (80, 140))

    status_text = font_text.render(
        f"Status: {player.get_status()}",
        True,
        BLACK
    )
    screen.blit(status_text, (80, 190))

    position = player.get_position_seconds()
    position_text = font_text.render(
        f"Position: {position} sec",
        True,
        BLACK
    )
    screen.blit(position_text, (80, 240))

    controls_title = font_text.render("Controls:", True, BLUE)
    screen.blit(controls_title, (80, 320))

    controls = [
        "P = Play",
        "S = Stop",
        "N = Next track",
        "B = Previous track",
        "Q = Quit"
    ]

    y = 370
    for control in controls:
        text = font_small.render(control, True, BLACK)
        screen.blit(text, (100, y))
        y += 35

    pygame.display.flip()


def main():
    running = True

    while running:
        draw_ui()

        if player.is_playing and not pygame.mixer.music.get_busy():
            player.next_track()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()

                elif event.key == pygame.K_s:
                    player.stop()

                elif event.key == pygame.K_n:
                    player.next_track()

                elif event.key == pygame.K_b:
                    player.previous_track()

                elif event.key == pygame.K_q:
                    running = False

        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()