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

health_bar = pygame.image.load("game_files/Health bar.png")

GUI_Buttons = {
     "fight":{
          "unselected": pygame.image.load("game_files/FINAL FIGHT UNSELECTED.png"),
          "selected": pygame.image.load("game_files/FINAL FIGHT.png")
     },

     "action":{
          "unselected": pygame.image.load("game_files/FINAL ACTION UNSELECTED.png"),
          "selected": pygame.image.load("game_files/FINAL ACTION.png")
     },

     "item":{
          "unselected": pygame.image.load("game_files/FINAL ITEM UNSELECTED.png"),
          "selected": pygame.image.load("game_files/FINAL ITEM.png")
     },

     "spare":{
          "unselected": pygame.image.load("game_files/FINAL SPARE UNSELECTED.png"),
          "selected": pygame.image.load("game_files/FINAL SPARE.png")
     }
}



                                 
FPS = 30

while running == True:

    surface.fill(BLACK)
    gameScreen.blit(GUI_Buttons["fight"]["unselected"], (0,530))
    gameScreen.blit(GUI_Buttons["action"]["unselected"], (250,530))
    gameScreen.blit(health_bar, (500,530))
    gameScreen.blit(GUI_Buttons["item"]["unselected"], (710,530))
    gameScreen.blit(GUI_Buttons["spare"]["unselected"], (960,530))

    
    
    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
print("\n\n\n\n\n\n\n\n")
sys.exit()