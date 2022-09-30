import view
import model, controller

import time

while True:
    time.sleep(1/100)
    controller.control()
    model.step()
    view.draw()