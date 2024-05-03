import unittest
import pygame
from event_box import *

class TestEB(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.test_eb = event_box(10,20,30,40)

    def test_init(self):
        self.assertEqual(self.test_eb.width, 30)
        self.assertEqual(self.test_eb.posX, 10)
        self.assertEqual(self.test_eb.posY, 20)
        self.assertEqual(self.test_eb.height, 40)
    
    def test_set_used(self):
        self.test_eb.set_used()
        self.assertTrue(self.test_eb.used)
