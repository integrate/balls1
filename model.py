import pygame, random

pygame.init()

mode_details=True

balls_per_second = 10
balls = []


def add_random_ball():
    size = random.randint(2, 5)
    x = random.randint(int(size / 2), 500 - int(size / 2))
    y = random.randint(int(size / 2), 500 - int(size / 2))
    r = random.randint(30, 255)
    g = random.randint(30, 255)
    b = random.randint(30, 255)
    speedx = random.randint(0, 4)
    speedy = random.randint(0, 4)

    ball = {"x":x, "y":y, "radius":size, "speedx":speedx, "speedy":speedy, "color": [r, g, b]}

    balls.append(ball)


def step():
    for ball in balls:
        ball["x"] += ball["speedx"]
        if ball["x"]+ball["radius"]/2 > 500:
            ball["speedx"] = -ball["speedx"]
            ball["x"] = 500-ball["radius"]/2

        if ball["x"]-ball["radius"]/2 < 0:
            ball["speedx"] = -ball["speedx"]
            ball["x"] = ball["radius"]/2

        ball["y"] += ball["speedy"]
        if ball["y"]+ball["radius"]/2 > 500:
            ball["speedy"] = -ball["speedy"]
            ball["y"] = 500-ball["radius"]/2

        if ball["y"]-ball["radius"]/2 < 0:
            ball["speedy"] = -ball["speedy"]
            ball["y"] = ball["radius"]/2