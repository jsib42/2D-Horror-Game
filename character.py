import pygame

class character:
    """

    Holds the basic information for each character.

    Attributes
        Name (str): Characters Name
        posX (int): X position of the character on screen
        posY (int): Y position of the character on screen
        dialouge (string array): array of dialouge the character is going to say
        can_move (bool): Flag for if the character is locked in place.

    """

    def __init__(self, name = "N/A", X = 0, Y = 0):

        """

        Parameters:
            Name - Gives the character a name.
        """

        self.Name = name
        self.posX = X
        self.posY = Y
        self.dialog_spoken = []
        self.dialog = []
        self.can_move = False
        self.dialog_index = 0
        self.is_monster = False

        self.id = f"{self.Name}"
        self.img = pygame.image.load(f"CharacterPixelArt/{self.id}.png").convert_alpha()
        self.img = pygame.transform.scale_by(self.img, 5)
        self.initialize_dialog()

    def initialize_dialog(self):
        file = open(f"CharacterDialog/{self.id}.txt")
        #print("File Opened")
        while True:
            line = file.readline()
            if not line:
                break
            #print(line)
            self.dialog.append(line)
            self.dialog_spoken.append(False)            
        file.close()
        #print("File Closed")

    def get_dialog_spoken(self, index):
        return self.dialog_spoken[index]

    def get_index(self):
        return self.dialog_index

    def inc_index(self):
        self.dialog_index = self.dialog_index + 1

    def set_dialog_spoken(self, index):
        self.dialog_spoken[index] == True

    def get_dialog(self, index):
        return self.dialog[index]

    def toggle_move(self):
        if self.can_move == False:
            self.can_move = True
        elif self.can_move == True:
            self.can_move = False

    def get_pos(self):
        return self.posX, self.posY

    def set_monster(self):
        self.is_monster = True

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_a]:
            self.posX = self.posX - dist
        if key[pygame.K_d]:
            self.posX = self.posX + dist
        if key[pygame.K_w]:
            self.posY = self.posY - dist
        if key[pygame.K_s]:
            self.posY = self.posY + dist

    def move_monster(self, speed, X, Y):
        if Y < self.posY:
            self.posY = self.posY - speed
            print("moved up")
        if X > self.posX:
            self.posX = self.posX + speed
            print("moved right")
        if X < self.posX:
            self.posX = self.posX - speed
            print("moved left")
        if Y > self.posY:
            self.posY = self.posY + speed
            print("moved down")
    
    def draw(self, canvas):
        canvas.blit(self.img, (self.posX, self.posY))