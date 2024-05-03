import pygame, pygame_gui
from settings import *

class dialog:
    def __init__(self, text = "N/A", character = " N/A "):
        self.name = character
        self.width = 1000
        self.height = 150
        self.posX = 100
        self.posY = 700
        self.line = text
        self.font = pygame.font.Font(None, 24)
        self.text_color = (255,255,255)
        self.manager = pygame_gui.UIManager((1600,900))
        if character != " N/A ":
            self.image = pygame.image.load(f"characterArt/{character}.png").convert_alpha()

    def draw(self, canvas):
        pygame.draw.rect(canvas, (31,35, 57), (self.posX, self.posY, self.width, self.height))
        pygame.draw.rect(canvas, BLACK, (self.posX, self.posY, self.width, self.height), 2)
        canvas.blit(self.image, (1150,200))
        rendered_text = self.font.render(self.line, True, (93,137,94))
        text_rect = rendered_text.get_rect(center=(self.posX + self.width // 2, self.posY + self.height // 2))
        character_text = self.font.render(self.name, True, self.text_color)
        character_rect = character_text.get_rect(topleft=(self.posX + 10, self.posY + 10))

        canvas.blit(character_text, character_rect)
        canvas.blit(rendered_text, text_rect)
        