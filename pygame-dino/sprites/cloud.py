import pygame
import random
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'assects\images\cloud.png')
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.midtop = surface.get_rect().midtop
        self.rect.x = surface.get_width()
        self.rect.y = random.randint(0, surface.get_height() / 2 - self.rect.height)
        self.speed = random.randint(1, 10)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
