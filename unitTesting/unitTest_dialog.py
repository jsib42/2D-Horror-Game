import unittest
import pygame
from dialog_manager import *

class TestEB(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.test_dialog = dialog("Test String")

    def test_init(self):
        self.assertEqual(self.test_dialog.width, 800)
        self.assertEqual(self.test_dialog.posX, 700)
        self.assertEqual(self.test_dialog.posY, 600)
        self.assertEqual(self.test_dialog.height, 250)
        self.assertEqual(self.test_dialog.line, "Test String")