import pygame

class character:
    """

    Holds the basic information for each character.

    Attributes
        Name (str): Characters Name
        PosX (int): X position of the character on screen
        PosY (int): Y position of the character on screen
        dialouge (string array): array of dialouge the character is going to say
        can_move (bool): Flag for if the character is locked in place.

    """

    def __init__(self, name = "N/A", X = 0, Y = 0):

        """

        Parameters:
            Name - Gives the character a name.
        """

        self.Name = name
        self.PosX = X
        self.PosY = Y
        self.dialouge_spoken = []
        self.dialouge = []
        self.can_move = False

        self.id = f"{self.Name}"
        self.img = pygame.image.load(f"CharacterPixelArt/{self.id}_scary.png").convert_alpha()
        self.img = pygame.transform.scale_by(self.img, 5)
        self.initialize_dialouge()

    def initialize_dialouge(self):
        file = open(f"CharacterDialouge/{self.id}.txt")
        #print("File Opened")
        while True:
            line = file.readline()
            if not line:
                break
            #print(line)
            self.dialouge.append(line)
            self.dialouge_spoken.append(False)            
        file.close()
        #print("File Closed")

    def get_dialouge_spoken(self, index):
        return self.dialouge_spoken[index]

    def set_dialouge_spoken(self, index):
        self.dialouge_spoken[index] == True

    def get_dialouge(self, index):
        return self.dialouge[index]

    def toggle_move(self):
        if self.can_move == False:
            self.can_move = True
        elif self.can_move == True:
            self.can_move = False

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_a]:
            self.PosX = self.PosX - dist
        if key[pygame.K_d]:
            self.PosX = self.PosX + dist
        if key[pygame.K_w]:
            self.PosY = self.PosY - dist
        if key[pygame.K_s]:
            self.PosY = self.PosY + dist
    
    def draw(self, canvas):
        # print(self.PosX)
        # print(self.PosY)
        canvas.blit(self.img, (self.PosX, self.PosY))