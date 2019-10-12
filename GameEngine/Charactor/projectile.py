import pygame
class bullet:
    def __init__(self, surface, player):
        self.surface = surface
        self.SpawningPoint = ((player.rectObj[0] + 5), (player.rectObj[1] + 20))
        self.rect = pygame.rect.Rect(self.SpawningPoint[0], self.SpawningPoint[1], 10, 10)
        self.isActive = False
        self.isReady = True
    def borderCheck(self):
        if self.rect[0] > 500:
            self.isActive = False

    def playerCheck(self, player):
        if not self.isActive and not self.rect.colliderect(player.rectObj):

            self.SpawningPoint = ((player.rectObj[0] + 5), (player.rectObj[1] + 20))
            if not self.rect[1] == self.SpawningPoint[1]:
                if self.rect[1] > self.SpawningPoint[1]:
                    self.rect[1] -= 6
                elif self.rect[1] < self.SpawningPoint[1]:
                    self.rect[1] += 6
            if not self.rect[0] == self.SpawningPoint[0]:
                if self.rect[0] > self.SpawningPoint[0]:
                    self.rect[0] -= 10
                elif self.rect[0] < self.SpawningPoint[0]:
                    self.rect[0] += 5

        if player.rectObj.colliderect(self.rect):
            self.isReady = True
            if not self.rect[1] == self.SpawningPoint[1]:
                if self.rect[1] > self.SpawningPoint[1]:
                    self.rect[1] -= 1
                elif self.rect[1] < self.SpawningPoint[1]:
                    self.rect[1] += 1

            self.rect[0] = self.SpawningPoint[0]

    def update(self):
        self.borderCheck()
        if self.isActive:
            self.rect.move_ip(10, 0)
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect)
