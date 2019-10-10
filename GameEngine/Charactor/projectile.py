import pygame
class bullet:
    def __init__(self, surface, player):
        self.surface = surface
        self.SpawningPoint = (player.rectObj[0], (player.rectObj[1] + 20))
        self.rect = pygame.rect.Rect(self.SpawningPoint[0], self.SpawningPoint[1], 10, 10)
        self.isActive = False
    def borderCheck(self):
        if self.rect[0] > 1001:
            self.isActive = False
            self.rect[0], self.rect[1] = self.SpawningPoint
    def update(self, player):
        self.SpawningPoint = (player.rectObj[0], (player.rectObj[1] + 20))
        self.borderCheck()
        if self.isActive:
            self.rect.move_ip(5, 0)
            pygame.draw.rect(self.surface, (255, 255, 255), self.rect)
