import pygame
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_run1 = pygame.image.load(r'assects\images\dinorun1.png')
        self.image_run2 = pygame.image.load(r'assects\images\dinorun2.png')
        self.sound_jump = pygame.mixer.Sound(r'assects\sounds\jump.wav')
        self.image = self.image_run1
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.midleft = surface.get_rect().midleft
        self.rect.x += 70
        self.rect.y -= 23
        self.step = 0
        self.height = 15
        self.jumping = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self):
        self.step += 1
        if self.step % 7 == 0:    
            if self.image == self.image_run1:
                self.image = self.image_run2
            else:
                self.image = self.image_run1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.sound_jump.play()
        if self.jumping:
            self.jump()
    def jump(self):
        self.rect.y -= self.height
        self.height -= 1
        if self.height < -15:
            self.height = 15
            self.jumping = False  