import pygame_widgets, pygame, ctypes, sys
from pygame import mixer
from button import *
from settings import *
from character import *
from background_manager import *
from dialog_manager import *
from event_box import *


class Game:

    def __init__(self):
        pygame.init()
        mixer.init()
        self.canvas = pygame.display.set_mode((1600,900))
        self.BM = background_manager()
        self.dialog = dialog()
        pygame.display.set_caption(TITLE)
        self.exit = False
        self.game_state = "main_menu"
        self.clock = pygame.time.Clock()
        mixer.music.load(MUSIC)
        mixer.music.set_volume(0.1)

        self.character = character("main", 70, 520)
        self.eb_dialog = event_box(70, 520, 50, 50)
        self.eb_up = event_box(1225,0, 100, 50)
        self.eb_right = event_box(1550, 300, 50, 100)
        self.get_images()
        self.create_buttons()

    def run(self):
        
        while True:
            events = pygame.event.get()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.game_state == "main_menu":
                self.canvas.blit(self.title_name_image, (600, 50))

                if self.play_button.draw(self.canvas):
                    self.game_state = "in_game"
                    mixer.music.play(-1,0.0,0)

                
                if self.settings_button.draw(self.canvas):
                    self.game_state = "settings"

                    #options

                if self.quit_button.draw(self.canvas):
                    pygame.quit()
                    sys.exit()
            if self.game_state == "settings":
                self.canvas.draw_text()

            if self.game_state == "in_game":
                self.BM.get_backgrounds()
                self.eb_dialog.draw_box(self.canvas)
                self.eb_up.draw_box(self.canvas)
                self.eb_right.draw_box(self.canvas)
                self.BM.show_background(self.canvas) 
                self.character.draw(self.canvas)
                self.character.handle_keys()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    mixer.music.pause()
                    paused = True

                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            
                        rect = pygame.rect.Rect((600, 200, 400, 350))
                        pygame.draw.rect(self.canvas, (255,255,255), rect)
                        if self.resume_button.draw(self.canvas):
                            mixer.music.play()
                            paused = False

                        if self.main_menu_button.draw(self.canvas):
                            self.game_state = "main_menu"
                            mixer.music.rewind()
                            paused = False
                        
                        if self.quit_button.draw(self.canvas):
                            pygame.quit()
                            sys.exit()
                        
                        pygame.display.update()
                        self.clock.tick(FPS)
                player_x, player_y = self.character.get_pos()
                if pygame.Rect(player_x, player_y, 50, 50).colliderect(self.eb_dialog.get_rect()) and self.eb_dialog.get_used() == False:
                    self.eb_dialog.set_used()
                    dialog_flag = True
                    self.character.toggle_move()
                    self.dialog = dialog(self.character.get_dialog(self.character.get_index()))
                    while dialog_flag:
                        key = pygame.key.get_pressed()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            self.dialog.draw(self.canvas)   
                            if key[pygame.K_SPACE] :
                                dialog_flag = False
                                self.character.toggle_move()

                            pygame.display.update()
                            self.clock.tick(FPS)
                if pygame.Rect(player_x, player_y, 50, 50).colliderect(self.eb_up.get_rect()) and self.eb_up.get_used() == False:
                    self.eb_up.set_used

                if pygame.Rect(player_x, player_y, 50, 50).colliderect(self.eb_right.get_rect()) and self.eb_right.get_used() == False:
                    self.eb_right.set_used


                

                


            pygame_widgets.update(events)
            pygame.display.update()
            self.canvas.fill(BACKGROUND_COLOR)
            self.clock.tick(FPS)

    def get_images(self):
        self.title_name_image = pygame.image.load("ButtonImages/title_name_image.png").convert_alpha()
        self.play_image = pygame.image.load("ButtonImages/play_image.png").convert_alpha()
        self.settings_image = pygame.image.load("ButtonImages/settings_image.png").convert_alpha()
        self.quit_image = pygame.image.load("ButtonImages/quit_image.png").convert_alpha()
        self.resume_image = pygame.image.load("ButtonImages/resume_image.png").convert_alpha()
        self.main_menu_image = pygame.image.load("ButtonImages/main_menu_image.png").convert_alpha()
    
    def create_buttons(self):
        self.play_button = Button(800, 300, self.play_image)
        self.settings_button = Button(800, 400, self.settings_image)
        self.quit_button = Button(800, 500, self.quit_image)
        self.resume_button = Button(800, 300, self.resume_image)
        self.main_menu_button = Button(800, 400, self.main_menu_image)


if __name__ == '__main__':
    game = Game()
    game.run()