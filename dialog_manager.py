import pygame, pygame_gui
from settings import *

class dialog:
    def __init__(self, text = "N/A", character = " N/A "):
        self.width = 800
        self.height = 250
        self.posX = 700
        self.posY = 600
        self.line = text
        self.font = pygame.font.Font(None, 24)
        self.text_color = BLACK
        self.manager = pygame_gui.UIManager((1600,900))
        if character != " N/A ":
            self.image = pygame.image.load(f"characterArt/{character}.png").convert_alpha()

    def draw(self, canvas):
        canvas.blit(self.image, (1000,0))
        pygame.draw.rect(canvas, GRAY, (self.posX, self.posY, self.width, self.height))
        self.font.size((700, 150))
        rendered_text = self.font.render(self.line, True, self.text_color)
        text_rect = rendered_text.get_rect(center=(self.posX + self.width // 2, self.posY + self.height // 2))

        canvas.blit(rendered_text, text_rect)
        