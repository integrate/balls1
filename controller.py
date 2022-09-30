import pygame
import model


BALL_ADD_TIMER = pygame.event.custom_type()
pygame.time.set_timer(BALL_ADD_TIMER, 10, 1)

def control():
    events = pygame.event.get()
    for e in events:
        if e.type==pygame.QUIT:
            exit()

        if e.type==pygame.KEYDOWN and e.key == pygame.K_e:
            model.mode_details = not model.mode_details

        if e.type==pygame.KEYDOWN and e.key == pygame.K_UP:
            model.inc_balls_per_second()

        if e.type==pygame.KEYDOWN and e.key == pygame.K_DOWN:
            model.dec_balls_per_second()

        if e.type==pygame.KEYDOWN and e.key == pygame.K_DELETE:
            model.clear_balls()

        if e.type==pygame.KEYDOWN and e.key == pygame.K_1:
            model.set_mode_stop()

        if e.type==pygame.KEYDOWN and e.key == pygame.K_2:
            model.set_mode_move()

        if e.type==pygame.KEYDOWN and e.key == pygame.K_3:
            model.set_mode_fall()

        if e.type == BALL_ADD_TIMER:
            if model.balls_per_second>0:
                model.add_random_ball()
            if model.balls_per_second>0:
                pygame.time.set_timer(BALL_ADD_TIMER, int(1000 / model.balls_per_second), 1)
            else:
                pygame.time.set_timer(BALL_ADD_TIMER, 10, 1)
