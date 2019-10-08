import pygame
import GameEngine.Charactor.playerObj as Charactor

class player:
    def __init__(self, surface, color, ground):
        self.surface = surface
        self.Player = Charactor.playerObj(self.surface, color)
        self.ground = ground
        self.jumpOrnot = False
        self.jumpV = False
        self.Flytime = 0
    def jump(self):
        y = self.Player.rectObj[1]
        key = pygame.key.get_pressed()

        if y >= 300 and not self.jumpV:
            self.Player.up(15)

        elif y <= 300 and self.Flytime < 20:
            if key[pygame.K_SPACE]:
                self.Flytime += 1
            else:
                self.Flytime = 20

        elif not self.Player.rectObj.colliderect(self.ground.groundRect) and self.Flytime >= 20:
            self.jumpV = True
            self.Player.down(10)
        else:
            self.jumpV = False
            self.jumpOrnot = False
            self.Flytime = 0
    def jumpChecks(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.jumpOrnot:
            self.jumpOrnot = True

        if self.jumpOrnot:

            self.jump()

    def checks(self):
        self.jumpChecks()

    def update(self):
        self.checks()
        self.Player.draw()
