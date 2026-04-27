import pygame
import random
import time

WIDTH, HEIGHT = 600, 800
LANES = [100, 200, 300]

class Player:
    def __init__(self, color):
        self.lane = 1
        self.y = 500
        self.color = color
        self.speed = 6
        self.powerup = None
        self.power_time = 0
        self.shield = False

    def move(self, direction):
        self.lane = max(0, min(2, self.lane + direction))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (LANES[self.lane]-20, self.y, 60, 80))


class Obstacle:
    def __init__(self):
        self.lane = random.randint(0, 2)
        self.y = -50
        self.type = random.choice(["car", "oil", "barrier"])

    def update(self, speed):
        self.y += speed

    def draw(self, screen):
        color = (255, 0, 0) if self.type == "car" else (0, 0, 0)
        pygame.draw.rect(screen, color, (LANES[self.lane]-20, self.y, 60, 80))


class PowerUp:
    def __init__(self):
        self.lane = random.randint(0, 2)
        self.y = -50
        self.type = random.choice(["nitro", "shield", "repair"])
        self.spawn_time = time.time()

    def update(self, speed):
        self.y += speed

    def draw(self, screen):
        color = {
            "nitro": (0, 255, 255),
            "shield": (0, 255, 0),
            "repair": (255, 255, 0)
        }[self.type]
        pygame.draw.circle(screen, color, (LANES[self.lane], int(self.y)), 10)


def run_game(settings, username):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player((255, 0, 0))
    obstacles = []
    powerups = []

    score = 0
    distance = 0
    speed = 6

    running = True

    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move(-1)
                if event.key == pygame.K_RIGHT:
                    player.move(1)

        speed += 0.001
        distance += speed

        if random.random() < 0.03:
            obstacles.append(Obstacle())

        if random.random() < 0.01:
            powerups.append(PowerUp())

        for obs in obstacles[:]:
            obs.update(speed)
            obs.draw(screen)

            if abs(obs.y - player.y) < 50 and obs.lane == player.lane:
                if player.shield:
                    player.shield = False
                    obstacles.remove(obs)
                else:
                    return {
                        "score": int(score),
                        "distance": int(distance),
                        "name": username
                    }

        for p in powerups[:]:
            p.update(speed)
            p.draw(screen)

            if time.time() - p.spawn_time > 5:
                powerups.remove(p)

            if abs(p.y - player.y) < 40 and p.lane == player.lane:
                player.powerup = p.type
                player.power_time = time.time()
                if p.type == "shield":
                    player.shield = True
                if p.type == "repair":
                    obstacles.clear()
                powerups.remove(p)

        if player.powerup == "nitro":
            if time.time() - player.power_time < 4:
                speed = 10
            else:
                player.powerup = None

        player.draw(screen)

        font = pygame.font.SysFont(None, 20)
        screen.blit(font.render(f"Score: {int(score)}", True, (255,255,255)), (10,10))
        screen.blit(font.render(f"Distance: {int(distance)}", True, (255,255,255)), (10,30))

        if player.powerup:
            screen.blit(font.render(f"Power: {player.powerup}", True, (255,255,0)), (10,50))

        score += 0.1

        pygame.display.flip()
        clock.tick(60)