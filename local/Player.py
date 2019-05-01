from Image import *

class Player():

    def __init__(self, ID, name, imageID, posX, posY):
        self.ID = ID
        self.name = name
        self.imageID = imageID
        self.posX = posX
        self.posY = posY

        self.nbBombs = 1

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
