import pygame_widgets, pygame, ctypes, sys
from button import *
from settings import *
from character import *
from background_manager import *


class Game:

    def __init__(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((1600,900))
        self.BM = background_manager()
        pygame.display.set_caption(" TBD ")
        self.exit = False
        self.game_state = "main_menu"
        self.clock = pygame.time.Clock()

        self.character = character("main")
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
                self.canvas.blit(self.title_name_image, (800, 100))

                if self.play_button.draw(self.canvas):
                    self.game_state = "in_game"

                
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
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    paused = True

                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            
                        rect = pygame.rect.Rect((600, 200, 400, 350))
                        pygame.draw.rect(self.canvas, (255,255,255), rect)
                        if self.resume_button.draw(self.canvas):
                            paused = False

                        if self.main_menu_button.draw(self.canvas):
                            self.game_state = "main_menu"
                            paused = False
                        
                        if self.quit_button.draw(self.canvas):
                            pygame.quit()
                            sys.exit()
                        
                        pygame.display.update()
                        self.clock.tick(FPS)

                self.BM.show_background(self.canvas)      
                self.character.draw(self.canvas)
                self.character.handle_keys()

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