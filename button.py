import pygame

class Button():

    def __init__(self, x, y, image):
        width = image.get_width()
        height = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center= (x,y)
        self.is_clicked = False

    def draw(self, canvas):
        clicked_flag = False
        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked_flag = True
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        canvas.blit(self.image, (self.rect.x, self.rect.y))

        return clicked_flag
