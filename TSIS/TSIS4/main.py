import pygame, json
from config import *
from game import Game
from db import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

create_tables()

def input_name():
    font = pygame.font.SysFont(None,30)
    name = ""
    while True:
        screen.fill((0,0,0))
        screen.blit(font.render("Username: "+name,True,(255,255,255)),(50,250))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RETURN: return name
                elif e.key==pygame.K_BACKSPACE: name=name[:-1]
                else: name+=e.unicode

def draw_menu():
    font = pygame.font.SysFont(None,40)
    opts = ["Play","Leaderboard","Settings","Quit"]
    for i,t in enumerate(opts):
        screen.blit(font.render(t,True,(255,255,255)),(200,150+i*80))

def leaderboard():
    data = get_top10()
    font = pygame.font.SysFont(None,20)
    while True:
        screen.fill((0,0,0))
        for i,row in enumerate(data):
            txt = f"{i+1}. {row[0]} {row[1]} L{row[2]}"
            screen.blit(font.render(txt,True,(255,255,255)),(50,50+i*40))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: exit()
            if e.type==pygame.KEYDOWN: return

def settings_screen():
    with open("settings.json") as f:
        s = json.load(f)

    font = pygame.font.SysFont(None,30)
    while True:
        screen.fill((0,0,0))
        screen.blit(font.render(f"Grid: {s['grid']}",True,(255,255,255)),(100,200))
        screen.blit(font.render(f"Sound: {s['sound']}",True,(255,255,255)),(100,260))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_g: s["grid"]=not s["grid"]
                if e.key==pygame.K_s: s["sound"]=not s["sound"]
                if e.key==pygame.K_RETURN:
                    with open("settings.json","w") as f:
                        json.dump(s,f)
                    return

username = input_name()
pid = get_or_create_player(username)
best = get_best_score(pid)

state = "menu"

while True:
    clock.tick(FPS)

    if state=="menu":
        screen.fill((0,0,0))
        draw_menu()
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_1: state="game"
                if e.key==pygame.K_2: leaderboard()
                if e.key==pygame.K_3: settings_screen()
                if e.key==pygame.K_4: exit()

    elif state=="game":
        game = Game(screen, pid, best)
        while True:
            clock.tick(game.speed)
            for e in pygame.event.get():
                if e.type==pygame.QUIT: exit()
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_LEFT: game.dx=-CELL; game.dy=0
                    if e.key==pygame.K_RIGHT: game.dx=CELL; game.dy=0
                    if e.key==pygame.K_UP: game.dx=0; game.dy=-CELL
                    if e.key==pygame.K_DOWN: game.dx=0; game.dy=CELL

            if not game.update():
                print("GAME OVER TRIGGERED")
                print("Saving:", pid, game.score, game.level)
                save_score(pid, game.score, game.level)
                break

            game.draw()
            pygame.display.flip()

        state="menu"