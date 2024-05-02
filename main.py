import pygame_widgets, pygame, ctypes, sys
from button import *
from settings import *


class Game:

    def __init__(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((1600,900))
        pygame.display.set_caption(" TBD ")
        self.exit = False
        self.game_state = "main_menu"
        self.clock = pygame.time.Clock()

        self.get_images()
        self.create_buttons()

    def run(self):
        
        while True:
            events = pygame.event.get()

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
    
    def create_buttons(self):
        self.play_button = Button(800, 300, self.play_image)
        self.settings_button = Button(800, 500, self.settings_image)
        self.quit_button = Button(800, 700, self.quit_image)


if __name__ == '__main__':
    game = Game()
    game.run()