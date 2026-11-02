import pygame
import sys
pygame.init()

gameScreen = pygame.display.set_mode((1200, 700))
surface = gameScreen
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
running = True

#COLOURS
BLACK = 0, 0, 0
WHITE = 255, 255, 255

player_heart_location = pygame.Vector2(600,450)


player_heart = pygame.image.load("game_files/player_heart.png")
fight = pygame.image.load("game_files/FINAL FIGHT.png")
action = pygame.image.load("game_files/FINAL ACTION.png")
item = pygame.image.load("game_files/FINAL ITEM.png")
spare = pygame.image.load("game_files/FINAL SPARE.png")

                                 
FPS = 30

while running == True:

    surface.fill(BLACK)
    pygame.draw.rect(surface, WHITE, (10, 530, 240, 120), 0)
    gameScreen.blit(fight,(10,530))
    pygame.draw.rect(surface, WHITE, (260, 530, 240, 120), 0)
    gameScreen.blit(action,(260,530))
    pygame.draw.rect(surface, WHITE, (510, 510, 180, 140), 0)
    #gameScreen.blit(fight,(,530))
    pygame.draw.rect(surface, WHITE, (700, 530, 240, 120), 0)
    gameScreen.blit(item,(700,530))
    pygame.draw.rect(surface, WHITE, (950, 530, 240, 120), 0)
    gameScreen.blit(spare,(950,530))
    gameScreen.blit(player_heart,(player_heart_location))
    

    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
print("\n\n\n\n\n\n\n\n")
sys.exit()