import pygame
from settings import *


class event_box:
    def __init__(self, X, Y, W, H):
        self.posX = X
        self.posY = Y
        self.width = W
        self.height = H
        self.used = False

    def set_used(self):
        self.used = True

    def get_used(self):
        return self.used

    def get_rect(self):
        return self.posX, self.posY, self.width, self.height

    def draw_box(self, canvas):
        pygame.draw.rect(canvas, GRAY, (self.posX, self.posY, self.width, self.height))