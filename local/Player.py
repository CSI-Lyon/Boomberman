from Image import *

class Player():

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.image = Image("skins/{}".format(ID), "face")
        
        self.nbBombs = 1

        self.posX = 1
        self.posY = 1

    def move(self, x, y):
        self.posX += x
        self.posY += y
