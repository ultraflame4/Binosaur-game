import pygame
class bullet:
    def __init__(self, surface, player):
        self.surface = surface
        self.SpawningPoint = (player.rectObj[0], (player.rectObj[1] + 20))
        self.rect = pygame.rect.Rect(self.SpawningPoint[0], self.SpawningPoint[1], 20, 10)
        self.isActive = False
        self.isReady = True
    def borderCheck(self):
        if self.rect[0] > 500:
            self.isActive = False

    def playerCheck(self, player):
        if not self.isActive:
            self.SpawningPoint = (player.rectObj[0], (player.rectObj[1] + 20))
            if not self.rect[1] == self.SpawningPoint[1]:
                if self.rect[1] > self.SpawningPoint[1]:
                    self.rect[1] -= 7
                elif self.rect[1] < self.SpawningPoint[1]:
                    self.rect[1] += 7
            if not self.rect[0] == self.SpawningPoint[0]:
                self.rect[0] -= 10

        if player.rectObj.colliderect(self.rect):
            self.isReady = True

    def update(self):
        self.borderCheck()
        if self.isActive:
            self.rect.move_ip(10, 0)
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect)
