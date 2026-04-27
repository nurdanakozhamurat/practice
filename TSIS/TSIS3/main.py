import pygame
from racer import run_game
from ui import main_menu
from persistence import *

pygame.init()
screen = pygame.display.set_mode((600,800))

settings = load_settings()

while True:
    choice = main_menu(screen)

    if choice == "play":
        username = "Player"
        result = run_game(settings, username)

        if result:
            save_score(result)

    elif choice == "leaderboard":
        data = load_leaderboard()
        print("\nTOP 10:")
        for i, d in enumerate(data):
            print(i+1, d)

    elif choice == "settings":
        settings["sound"] = not settings["sound"]
        save_settings(settings)
        print("Sound toggled")

    elif choice == "quit":
        break