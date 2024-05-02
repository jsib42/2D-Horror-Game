import pygame

class background_manager:
    def __init__(self):
        self.currentBackground = []
        self.id_up = 0
        self.id_right = 0
        self.currentBackground.append(pygame.image.load(f"Background_Images/{self.id_up}{self.id_right}-1.png").convert_alpha())
        self.currentBackground.append(pygame.image.load(f"Background_Images/{self.id_up}{self.id_right}-2.png").convert_alpha())

    def get_backgrounds(self):
        self.currentBackground[0] = pygame.image.load(f"Background_Images/{self.id_up}{self.id_right}-1.png").convert_alpha()
        self.currentBackground[1] = pygame.image.load(f"Background_Images/{self.id_up}{self.id_right}-2.png").convert_alpha()

    def increment_up(self):
        self.id_up = self.id_up + 1

    def increment_right(self):
        self.id_right = self.id_right + 1

    def show_background(self, canvas):
        canvas.blit(self.currentBackground[0], (-200,0))
        canvas.blit(self.currentBackground[1], (700,0))