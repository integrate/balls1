import pygame

import model

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Шариковый беспредел")

details_font = pygame.font.SysFont("Arial", 16, True)

def draw():
    screen.fill([0, 0, 0])

    for ball in model.balls:
        pygame.draw.circle(screen, ball["color"], [ball["x"], ball["y"]], ball["radius"])

    if model.mode_details:
        draw_details()

    pygame.display.flip()

def draw_details():
    details = [
        "E: скрыть/показать детали",
        "Шариков в секунду: " + str(model.balls_per_second) + " ВВЕРХ: увел, ВНИЗ: уменьш",
        "Шариков на экране:" + str(len(model.balls))+" DEL: очистить",
        " ",
        "Режимы: 1-стоп, 2-свободный полет, 3-падение"
    ]

    y = 10
    for det in details:
        t = details_font.render(det, True, [255, 74, 34], [250, 250, 250])
        t=t.convert_alpha()
        t.set_alpha(180)
        y+=20
        screen.blit(t, [10, y])