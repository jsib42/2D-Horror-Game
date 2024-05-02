import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((1600,900))
        pygame.display.set_caption(" TBD ")
        self.exit = False
        self.game_sate = "main_menu"



    def run(self):
        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.run()