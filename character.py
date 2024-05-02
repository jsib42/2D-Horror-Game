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
        self.dialog_spoken = []
        self.dialog = []
        self.can_move = False
        self.dialog_index = 0

        self.id = f"{self.Name}"
        self.img = pygame.image.load(f"CharacterPixelArt/{self.id}_front.png").convert_alpha()
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
        return self.PosX, self.PosY

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