import pygame
import sys
import json
import random

GUI_Buttons = { #menu boxes are 240 by 120
    "fight": {
        "unselected": pygame.image.load("game_files/FINAL FIGHT UNSELECTED.png"),
        "selected": pygame.image.load("game_files/FINAL FIGHT.png")
    },

    "action": {
        "unselected": pygame.image.load("game_files/FINAL ACTION UNSELECTED.png"),
        "selected": pygame.image.load("game_files/FINAL ACTION.png")
    },

    "item": {
        "unselected": pygame.image.load("game_files/FINAL ITEM UNSELECTED.png"),
        "selected": pygame.image.load("game_files/FINAL ITEM.png")
    },

    "spare": {
        "unselected": pygame.image.load("game_files/FINAL SPARE UNSELECTED.png"),
        "selected": pygame.image.load("game_files/FINAL SPARE.png")
    },

    "health": {
        "numbers": pygame.image.load("game_files/Health Bar numbers.png"),
        "no numbers": pygame.image.load("game_files/Health Bar no numbers.png")
    }
}

main_menu_sprites = {
    "menu backgrounds": {
        "main_menu_logo": pygame.image.load("game_files/main menu.png"),
        "settings": pygame.image.load("game_files/blank settings.png")
    },

    "start": {  #these are 200 by 100 pixels
        "selected": pygame.image.load("game_files/MENU START selected.png"),
        "unselected": pygame.image.load("game_files/MENU START.png")
    },

    "settings": {   #these are 200 by 100 pixels
        "selected": pygame.image.load("game_files/settings START selected.png"),
        "unselected": pygame.image.load("game_files/settings START.png"),
    },

    "keybinders": {

        "arrows": {
            "selected": pygame.image.load("game_files/ARROW selected.png"),
            "unselected": pygame.image.load("game_files/ARROW unselected.png"),
            "symbol": pygame.image.load("game_files/arrows symbol.png")
        },

        "wasd": {
            "selected": pygame.image.load("game_files/WASD selected.png"),
            "unselected": pygame.image.load("game_files/WASD unselected.png"),
            "symbol": pygame.image.load("game_files/WASD symbol.png")

        }
    }
}

# COLOURS
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0

with open("game_files/dialogue.json") as enemy_dialogue:
    dialogue = json.load(enemy_dialogue)



pygame.font.init()
pygame.init()
font_size = 25
game_font = pygame.font.Font("game_files/Arena.ttf", font_size)



gameScreen = pygame.display.set_mode((1200, 700))
surface = gameScreen
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
running = True

player_health = 16


menu_mode = True

settings_mode = False #is user in settings
keybinds = True #true is arrows, false is wasd
health_numbers = False #tru is numbers, flase is without numbers
settings_position = 1 # 1- arrows, 2- wasd 3- health
settings_health_yellow_check = WHITE
main_menu_selected = True #true is start, false is settings

user_turn_selection = 1 #1-4 is fight to spare accordingly

fight_stage = 0 #0 is not turned on, 1 is prehit dialogue, just incase you want to back out, 2 is the quick time and 3 is the post hit dialogue



player_heart_location = pygame.Vector2(600, 450)
player_heart = pygame.image.load("game_files/player heart.png")
health_bar = GUI_Buttons["health"]["no numbers"]

one_hp_bar_length = 12
one_hp_bar_height = 74


battle_box_sides_length = 350


is_user_in_battle = False



FPS = 30

def draw_health_bar(health):
    gameScreen.blit(health_bar, (500, 530))
    pygame.draw.rect(gameScreen, BLACK, (696 - (16 - health)*one_hp_bar_length, 570, (16 - health)*one_hp_bar_length, one_hp_bar_height), 0)


def draw_menu_boxes(box_to_highlight):
    if box_to_highlight == 0:
        gameScreen.blit(GUI_Buttons["fight"]["unselected"], (0, 530))
        gameScreen.blit(GUI_Buttons["action"]["unselected"], (250, 530))
        gameScreen.blit(GUI_Buttons["item"]["unselected"], (710, 530))
        gameScreen.blit(GUI_Buttons["spare"]["unselected"], (960, 530))
    
    elif box_to_highlight == 1:
        gameScreen.blit(GUI_Buttons["fight"]["selected"], (0, 530))
        gameScreen.blit(GUI_Buttons["action"]["unselected"], (250, 530))
        gameScreen.blit(GUI_Buttons["item"]["unselected"], (710, 530))
        gameScreen.blit(GUI_Buttons["spare"]["unselected"], (960, 530))

    elif box_to_highlight == 2:
        gameScreen.blit(GUI_Buttons["fight"]["unselected"], (0, 530))
        gameScreen.blit(GUI_Buttons["action"]["selected"], (250, 530))
        gameScreen.blit(GUI_Buttons["item"]["unselected"], (710, 530))
        gameScreen.blit(GUI_Buttons["spare"]["unselected"], (960, 530))

    elif box_to_highlight == 3:
        gameScreen.blit(GUI_Buttons["fight"]["unselected"], (0, 530))
        gameScreen.blit(GUI_Buttons["action"]["unselected"], (250, 530))
        gameScreen.blit(GUI_Buttons["item"]["selected"], (710, 530))
        gameScreen.blit(GUI_Buttons["spare"]["unselected"], (960, 530))

    elif box_to_highlight == 4:
        gameScreen.blit(GUI_Buttons["fight"]["unselected"], (0, 530))
        gameScreen.blit(GUI_Buttons["action"]["unselected"], (250, 530))
        gameScreen.blit(GUI_Buttons["item"]["unselected"], (710, 530))
        gameScreen.blit(GUI_Buttons["spare"]["selected"], (960, 530))
            
def change_health_numbers():
    if settings_position == 3:
        settings_health_yellow_check = YELLOW
        game_font.set_underline(True)
    elif settings_position != 3:
        settings_health_yellow_check = WHITE
        game_font.set_underline(False)

    if health_numbers == False:
        health_bar = GUI_Buttons["health"]["no numbers"]
        text_surface = game_font.render("Your HEALTH is blank", True, settings_health_yellow_check)
        gameScreen.blit(text_surface, (475, 270))
        gameScreen.blit(GUI_Buttons["health"]["no numbers"], (500, 305))

    elif health_numbers == True:
        health_bar = GUI_Buttons["health"]["numbers"]
        text_surface = game_font.render("Your HEALTH has numbers", True, settings_health_yellow_check)
        gameScreen.blit(text_surface, (475, 270))
        gameScreen.blit(GUI_Buttons["health"]["numbers"], (500, 305))



def change_keybinders():
    if keybinds == True:
        gameScreen.blit(main_menu_sprites["keybinders"]["arrows"]["symbol"], (575,215))
    else:
        gameScreen.blit(main_menu_sprites["keybinders"]["wasd"]["symbol"], (575,215))

    if settings_position == 1:
        gameScreen.blit(main_menu_sprites["keybinders"]["arrows"]["selected"], (400,100))
        gameScreen.blit(main_menu_sprites["keybinders"]["wasd"]["unselected"], (605, 100))

    elif settings_position == 2:
        gameScreen.blit(main_menu_sprites["keybinders"]["arrows"]["unselected"], (400,100))
        gameScreen.blit(main_menu_sprites["keybinders"]["wasd"]["selected"],(605, 100))

    elif settings_position != 1 or 2:
        gameScreen.blit(main_menu_sprites["keybinders"]["arrows"]["unselected"], (400,100))
        gameScreen.blit(main_menu_sprites["keybinders"]["wasd"]["unselected"], (605, 100))
escape_counter = 0

def escape_with_key():
    escape_counter = 0
    if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
        escape_counter += 1
        fading_text = game_font.render("Exiting game...", True, WHITE)
        fading_text.set_alpha(255-(3*escape_counter))
        gameScreen.blit(fading_text,(100,100))
        if escape_counter == 85:
            running = False
            return running
        else:
            escape_counter = 0





random_fight_prehit_dialogue = random.randint(0,2)


while running == True:
    escape_with_key()



    if menu_mode == True:

        if settings_mode == False:

            gameScreen.blit(main_menu_sprites["menu backgrounds"]["main_menu_logo"],(0, 0))

            if main_menu_selected == True:
                gameScreen.blit(main_menu_sprites["start"]["selected"], (500, 300))
                gameScreen.blit(main_menu_sprites["settings"]["unselected"], (500, 420))

            elif main_menu_selected == False:
                gameScreen.blit(main_menu_sprites["start"]["unselected"], (500, 300))
                gameScreen.blit(main_menu_sprites["settings"]["selected"], (500, 420))



        elif settings_mode == True:
            gameScreen.blit(main_menu_sprites["menu backgrounds"]["settings"],(0, 0))
            change_health_numbers()            
            change_keybinders()
            





    elif menu_mode == False:

        surface.fill(BLACK)

        

        if is_user_in_battle == True:
            draw_menu_boxes(0)
            draw_health_bar(player_health)


            pygame.draw.rect(gameScreen,WHITE,(425, 175, battle_box_sides_length, battle_box_sides_length),3) #battle box
            #gameScreen.blit(player_heart, player_heart_location)

        elif is_user_in_battle == False:
            draw_menu_boxes(0)
            draw_health_bar(player_health)
            
            
            pygame.draw.rect(gameScreen, WHITE, (50, 370, 1100, 150), 5)  # dialogue box
            text_surface = game_font.render(dialogue["fight"]["prehit"][random_fight_prehit_dialogue], True, WHITE)
            gameScreen.blit(text_surface, (70, 390))


    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if menu_mode == True:
                    if settings_mode == False:
                        main_menu_selected = not main_menu_selected

                    elif settings_mode == True:
                        settings_position -= 2
                        settings_position = max(settings_position, 1)


            elif event.key == pygame.K_DOWN:
                if menu_mode == True:
                    if settings_mode == False:
                        main_menu_selected = not main_menu_selected

                    elif settings_mode == True:
                        settings_position += 2
                        settings_position = min(settings_position, 3)


            elif event.key == pygame.K_LEFT:
                if menu_mode == True:
                    if settings_mode == False:
                        main_menu_selected = not main_menu_selected


                    elif settings_mode == True:
                        settings_position -= 1
                        settings_position = max(settings_position, 1)


            elif event.key == pygame.K_RIGHT:
                if menu_mode == True:
                    if settings_mode == False:
                        main_menu_selected = not main_menu_selected
                    
                    elif settings_mode == True:
                        settings_position += 1
                        settings_position = min(settings_position,3)




            elif event.key == pygame.K_u:
                player_health -= 1
                print(player_health)

            elif event.key == pygame.K_i:
                player_health += 1
                print(player_health)
                
            elif event.key == pygame.K_y:
                #random_fight_prehit_dialogue = random.randint(0,2)
                health_numbers = not health_numbers


            elif event.key == pygame.K_z:
                if main_menu_selected == False:
                    settings_mode = True
                    if settings_position == 1:
                        keybinds = True
                    elif settings_position == 2:
                        keybinds = False
                    elif settings_position == 3:
                        health_numbers = not health_numbers

                elif main_menu_selected == True:
                    menu_mode = False


            elif event.key == pygame.K_x:
                if settings_mode == True:
                    settings_mode = False
                    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        print("escaping gamein ", escape_counter/30, "seconds!")

    if keys[pygame.K_LEFT]:
        print("LEFT is being held")

    if keys[pygame.K_RIGHT]:
        print("RIGHT is being held")

    if keys[pygame.K_UP]:
        print("UP is being held")

    if keys[pygame.K_DOWN]:
        print("DOWN is being held")


pygame.quit()
print("\n\n\n\n\n\n\n\n")
sys.exit()