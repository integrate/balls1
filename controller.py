import pygame
import model


BALL_ADD_TIMER = pygame.event.custom_type()
pygame.time.set_timer(BALL_ADD_TIMER, int(1000/model.balls_per_second), 1)

def control():
    events = pygame.event.get()
    for e in events:
        if e.type==pygame.QUIT:
            exit()

        if e.type==pygame.KEYDOWN and e.key == pygame.K_e:
            model.mode_details = not model.mode_details

        if e.type == BALL_ADD_TIMER:
            model.add_random_ball()
            pygame.time.set_timer(BALL_ADD_TIMER, int(1000 / model.balls_per_second), 1)

