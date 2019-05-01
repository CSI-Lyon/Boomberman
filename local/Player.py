from Image import *

class Player():

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.image = Image("skins/{}".format(ID), "down")

        self.nbBombs = 1

        self.posX = 1
        self.posY = 1

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def go(self, direction):
        if direction == "Up":
            self.posY -= 1
        elif direction == "Right":
            self.posX += 1
        elif direction == "Down":
            self.posY += 1
        else:
            self.posX -= 1
