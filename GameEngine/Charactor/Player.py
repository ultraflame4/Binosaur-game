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
        self.Leve = 0
    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.Leve < 10:
            self.Leve += 5
        else:
            self.Leve = 0

        if self.jumpVar < 100 and not self.jumped:
            self.Player.up(10)
            self.jumpVar += 5
        elif self.jumpVar >= 100 and not self.Leve:
            self.jumped = True
            if not self.Player.rectObj.colliderect(self.ground.groundRect):
                self.Player.down(10)
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
