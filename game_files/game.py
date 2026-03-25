import pygame
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.font.init()


screenLengthX = 800
screenHeightY = 600

BattleBoxLengthX = 0

BattleState = False

screen = pygame.display.set_mode((screenLengthX, screenHeightY))
surface = screen
pygame.display.set_caption("My Game")

BLACK = 0, 0, 0
GREY40 = 40, 40, 40
WHITE = 255, 255, 255


clock = pygame.time.Clock()
running = True

HealthBar = pygame.image.load(os.path.join(BASE_DIR, "Health.png"))
Fight = pygame.image.load(os.path.join(BASE_DIR, "FightDeselected.png"))
Act = pygame.image.load(os.path.join(BASE_DIR, "ActSelected.png"))
Item = pygame.image.load(os.path.join(BASE_DIR, "ItemDeselected.png"))
Spare = pygame.image.load(os.path.join(BASE_DIR, "SpareDeselected.png"))
Heart = pygame.image.load(os.path.join(BASE_DIR, "Heart.png"))

heightTest = 50
HeightTest1 = 538
playerBodyLocationX = 390
playerBodyLocationY = 340


def Bullet():
    pass

movementSpeedIncrement = 3

while running == True:
    surface.fill(BLACK)
    pygame.draw.rect(surface, WHITE, (200, 200, 400, 300), 2)
    surface.blit(Heart ,(playerBodyLocationX, playerBodyLocationY))
    #pygame.draw.rect(surface, WHITE, (50, 50, 160, 90), 0)
    screen.blit(Fight, (115,538))
    screen.blit(Act, (230,538))
    screen.blit(Item, (460,538))
    screen.blit(Spare, (575,538))
    #pygame.draw.rect(surface, WHITE, (345, HeightTest1, 110, heightTest))
    screen.blit(HealthBar, (345,503,110,80))


    pygame.display.flip()
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print("B was presssed")
                Bullet()

            if event.key ==  pygame.K_x:
                BattleState = not BattleState
                print("X was presssed")
                heightTest += 5
                HeightTest1 -= 5
                print(HeightTest1)
                print(heightTest)

    keyState = pygame.key.get_pressed()

    if keyState[pygame.K_LEFT]:
        playerBodyLocationX -= movementSpeedIncrement
        playerBodyLocationX = max(playerBodyLocationX, 202)
    if keyState[pygame.K_RIGHT]:
        playerBodyLocationX += movementSpeedIncrement
        playerBodyLocationX = min(playerBodyLocationX, 577)
    if keyState[pygame.K_UP]:
        playerBodyLocationY -= movementSpeedIncrement
        playerBodyLocationY = max(playerBodyLocationY, 202)
    if keyState[pygame.K_DOWN]:
        playerBodyLocationY += movementSpeedIncrement
        playerBodyLocationY = min(playerBodyLocationY, 478)





pygame.quit()
print("\n\n\n\n\n\n\n\n")
sys.exit()