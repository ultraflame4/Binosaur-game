import pygame
import GameEngine.Charactor.playerObj as Charactor

class player:
    def __init__(self, surface, color, ground):
        self.surface = surface
        self.Player = Charactor.playerObj(self.surface, color)
        self.ground = ground
        self.jumpVar = 0
        self.jumped = False
        self.jumpOrnot = False
    def jump(self):
        if self.jumpVar < 11 and not self.jumped:
            self.Player.up()
            self.jumpVar += 1
        elif self.jumpVar >= 11:
            self.jumped = True
            if not self.Player.rectObj.colliderect(self.ground.groundRect):
                self.Player.down()
            else:
                self.jumped = False
                self.jumpVar = 0
                self.jumpOrnot = False
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
