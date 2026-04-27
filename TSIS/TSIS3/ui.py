import pygame

def draw_text(screen, text, y):
    font = pygame.font.SysFont(None, 40)
    txt = font.render(text, True, (255,255,255))
    rect = txt.get_rect(center=(200, y))
    screen.blit(txt, rect)


def main_menu(screen):
    while True:
        screen.fill((0,0,0))
        draw_text(screen, "PLAY (P)", 200)
        draw_text(screen, "LEADERBOARD (L)", 250)
        draw_text(screen, "SETTINGS (S)", 300)
        draw_text(screen, "QUIT (Q)", 350)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return "play"
                if event.key == pygame.K_l:
                    return "leaderboard"
                if event.key == pygame.K_s:
                    return "settings"
                if event.key == pygame.K_q:
                    return "quit"