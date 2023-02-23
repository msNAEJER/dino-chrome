import pygame
class Score(pygame.sprite.Sprite):
    def __init__(self, step = 0, points = -1):
        super().__init__()
        self.step = step
        self.points = points
        self.font = pygame.font.Font(r'assects\font\gamefont.ttf', 20)
        self.image = self.font.render(f'HI {self.points}', True, (20, 232, 255))
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.midright = surface.get_rect().midright
        self.rect.y -= 70
        self.rect.x -= 30
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f'HI {self.points}', True, (20, 232, 255))
class GameOver(pygame.sprite.Sprite):
    def __init__(self, step = 0, points = -1):
        super().__init__()
        self.font = pygame.font.Font(r'assects\font\gamefont.ttf', 25)
        self.image1 = self.font.render(f'G A M E  O V E R', True, (250, 2, 2))
        self.image2 = pygame.image.load(r'assects\images\reset.png')
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        surface = pygame.display.get_surface()
        self.rect1.center = surface.get_rect().center
        self.rect1.y-=80
        self.rect2.center = surface.get_rect().center
    def draw(self, surface):
        surface.blit(self.image1, self.rect1)
        surface.blit(self.image2, self.rect2)
        self.image1 = self.font.render(f'G A M E  O V E R', True, (250, 2, 2))