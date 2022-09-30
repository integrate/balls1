import pygame

import model

pygame.init()

screen = pygame.display.set_mode([500, 500])


details_font = pygame.font.SysFont("Arial", 20, True)

def draw():
    screen.fill([0, 0, 0])
    if model.mode_details:
        draw_details()

    for ball in model.balls:
        pygame.draw.circle(screen, ball["color"], [ball["x"], ball["y"]], ball["radius"])

    pygame.display.flip()

def draw_details():
    details = [
        "E: скрыть/показать детали",
        "Шариков в секунду: " + str(model.balls_per_second),
        "Шариков на экране:" + str(len(model.balls))
    ]

    y = 10
    for det in details:
        t = details_font.render(det, True, [255, 74, 34])
        t=t.convert_alpha()
        t.set_alpha(50)
        y+=20
        screen.blit(t, [10, y])