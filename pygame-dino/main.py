import pygame
import sys
from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.obstacles import Cactus
from sprites.game import Score
from sprites.game import GameOver
pygame.init()  


# Константы
WIDTH = 700
HEIGHT = 500
fps = 60
surf1 = pygame.Surface((WIDTH, HEIGHT - 250))
surf1.fill((98, 180, 227))
surf2 = pygame.Surface((WIDTH, HEIGHT - 250))
surf2.fill((252, 237, 18))
# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()
pygame.display.update()
def main():
    global fps
    # Спрайты
    road = Road()
    clouds = pygame.sprite.Group()
    player = Dino()
    obstacles = pygame.sprite.Group()
    score = Score()
    gameover = GameOver()
    game_over = False
    running = True
    while running:
        # Частота обновления экрана
        clock.tick(fps)


        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    main()
        for obstacle in obstacles:
            if pygame.sprite.collide_mask(player, obstacle) and not game_over:
                fps = 60
                game_over = True
                end = GameOver() 
        # Рендеринг
        screen.fill((255, 255, 255))
        screen.blit(surf1, (0, 0))
        screen.blit(surf2, (0, 250))
        road.draw(screen)
        clouds.draw(screen)
        player.draw(screen)    
        score.draw(screen)
        obstacles.draw(screen)    
        if game_over:
            end.draw(screen)
        
        # Обновление спрайтов
        if not game_over:
            road.update()
            clouds.update()
            player.update()
            obstacles.update()
            score.update()
        if len(clouds) < 3:
            cloud = Cloud()
            clouds.add(cloud)
        if len(obstacles) < 1:
            cactus = Cactus()
            obstacles.add(cactus)
            fps += 2
            score.points += 1
        
        # Обновление экрана
        pygame.display.update()
    player.jump()
if __name__ == '__main__':
    main()