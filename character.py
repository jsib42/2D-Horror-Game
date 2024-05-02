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

    def __init__(self, name = "N/A"):

        """

        Parameters:
            Name - Gives the character a name.
        """

        self.Name = name
        self.PosX = 0
        self.PosY = 0
        self.dialouge = []
        self.can_move = False

        self.id = f"{self.Name}"
        self.img = pygame.image.load(f"CharacterPixelArt/{self.id}.png").convert_alpha()



    def toggle_move(self):
        if self.can_move == False:
            self.can_move = True
        elif self.can_move == True:
            self.can_move = False