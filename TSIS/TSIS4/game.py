import pygame, random, json
from config import *

class Game:
    def __init__(self, screen, player_id, best):
        self.screen = screen
        self.player_id = player_id
        self.best = best

        self.load_settings()
        self.reset()

    def load_settings(self):
        with open("settings.json") as f:
            self.settings = json.load(f)

    def reset(self):
        self.snake = [(100,100)]
        self.dx, self.dy = CELL, 0

        self.food = self.rand()
        self.poison = self.rand()

        self.powerup = None
        self.power_spawn_time = 0
        self.active_power = None
        self.power_end_time = 0

        self.obstacles = []

        self.score = 0
        self.level = 1
        self.speed = FPS

    def rand(self):
        return (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))

    def spawn_powerup(self):
        types = ["speed", "slow", "shield"]
        self.powerup = (self.rand(), random.choice(types))
        self.power_spawn_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()

        if not self.powerup and random.randint(0,100) < 2:
            self.spawn_powerup()

        if self.powerup and now - self.power_spawn_time > 8000:
            self.powerup = None

        if self.active_power and now > self.power_end_time:
            self.active_power = None
            self.speed = FPS + (self.level-1)*2

        head = (self.snake[0][0]+self.dx, self.snake[0][1]+self.dy)

        if head in self.snake or head in self.obstacles or head[0]<0 or head[1]<0 or head[0]>=WIDTH or head[1]>=HEIGHT:
            if self.active_power == "shield":
                self.active_power = None
            else:
                return False

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 10
            self.food = self.rand()

        elif head == self.poison:
            if len(self.snake) <= 2:
                return False
            self.snake = self.snake[:-2]
            self.poison = self.rand()

        elif self.powerup and head == self.powerup[0]:
            t = self.powerup[1]
            self.active_power = t
            self.powerup = None

            if t == "speed":
                self.speed += 5
                self.power_end_time = now + 5000
            elif t == "slow":
                self.speed = max(3, self.speed-3)
                self.power_end_time = now + 5000
            elif t == "shield":
                pass

        else:
            self.snake.pop()

        if self.score // 50 + 1 > self.level:
            self.level += 1
            self.speed += 2
            if self.level >= 3:
                self.add_obstacles()

        return True

    def add_obstacles(self):
        for _ in range(5):
            pos = self.rand()
            if pos not in self.snake:
                self.obstacles.append(pos)

    def draw(self):
        self.screen.fill((0,0,0))

        # grid
        if self.settings["grid"]:
            for x in range(0, WIDTH, CELL):
                pygame.draw.line(self.screen,(40,40,40),(x,0),(x,HEIGHT))
            for y in range(0, HEIGHT, CELL):
                pygame.draw.line(self.screen,(40,40,40),(0,y),(WIDTH,y))

        for s in self.snake:
            pygame.draw.rect(self.screen, self.settings["snake_color"], (*s,CELL,CELL))

        pygame.draw.rect(self.screen,(255,255,0),(*self.food,CELL,CELL))
        pygame.draw.rect(self.screen,(150,0,0),(*self.poison,CELL,CELL))

        for o in self.obstacles:
            pygame.draw.rect(self.screen,(100,100,100),(*o,CELL,CELL))

        if self.powerup:
            color = {"speed":(0,255,255),"slow":(0,0,255),"shield":(255,255,255)}
            pygame.draw.rect(self.screen,color[self.powerup[1]],(*self.powerup[0],CELL,CELL))

        font = pygame.font.SysFont(None,30)
        txt = font.render(f"{self.score} L{self.level} Best:{self.best}",True,(255,255,255))
        self.screen.blit(txt,(10,10))