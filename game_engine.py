import pygame, pygame_widgets
from settings import *

character_names['main', 'spirit']

class engine:
    def __init__(self, characters):
        self.characters = []
        self.get_characters
        
    
    def start_dialouge(self, character_id ,trigger_number):
        if self.characters[character_id].get_dialouge_spoken(trigger_number) == False:
            self.characters[character_id].toggle_move()
            text = self.characters[character_id].get_dialouge(trigger_number)
            self.characters[character_id].set_dialouge_spoken(trigger_number)

    def get_characters(self):
        for char in character_names:
            new_character = character(char, 70, 520)
