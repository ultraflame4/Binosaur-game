#! venv\Scripts\python
import pygame
import GameEngine
pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('The Bino Game')
Gui = GameEngine.mainDraw.mainGui(screen, (0,0,0))
run = True


while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False

    Gui.update()
    pygame.display.update()
