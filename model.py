import pygame, random

pygame.init()

mode_details=True

balls_per_second = 0
balls = []

mode="move"

def inc_balls_per_second():
    global balls_per_second
    balls_per_second+=1

def dec_balls_per_second():
    global balls_per_second
    balls_per_second-=1
    if balls_per_second<0:
        balls_per_second=0

def add_random_ball():
    size = random.randint(2, 5)
    x = random.randint(int(size / 2), 500 - int(size / 2))
    y = random.randint(int(size / 2), 500 - int(size / 2))
    r = random.randint(30, 255)
    g = random.randint(30, 255)
    b = random.randint(30, 255)
    speedx = random.randint(1, 4)
    speedy = random.randint(1, 4)

    ball = {"x":x, "y":y, "radius":size, "speedx":speedx, "speedy":speedy, "speed_y_fall":0, "color": [r, g, b]}

    balls.append(ball)

def clear_balls():
    balls.clear()

def set_mode_stop():
    global mode
    mode="stop"

def set_mode_move():
    global mode
    mode="move"

def set_mode_fall():
    global mode
    mode="fall"

def step():
    if mode=="move":
        move_balls()
    elif mode=="fall":
        fall_balls()

def move_balls():
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

def fall_balls():
    for ball in balls:
        ball["speed_y_fall"]+=0.05
        ball["y"]+=ball["speed_y_fall"]

        if ball["y"]+ball["radius"]/2 > 498:
            zamedl = 1.6/ball["radius"]
            ball["speed_y_fall"] = -ball["speed_y_fall"]*zamedl
            ball["y"] = 498 - ball["radius"] / 2

