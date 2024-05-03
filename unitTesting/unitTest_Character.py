import unittest
import pygame
from character import character 

class TestCharacter(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((800,500))
        self.test_character = character("main", 50, 100)

    def test_init(self):
        self.assertEqual(self.test_character.Name, 'main')
        self.assertEqual(self.test_character.posX, 50)
        self.assertEqual(self.test_character.posY, 100)
        self.assertFalse(self.test_character.can_move)
        
    def test_get_dialog(self):
        file = open(f"CharacterDialog/{self.test_character.id}.txt")
        line = file.readline()
        self.assertEqual(self.test_character.get_dialog(self.test_character.dialog_index), line)
        file.close()
