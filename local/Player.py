from Image import *

class Player():

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.image = Image("skins/{}".format(ID), "face")

        self.nbBombs = 1

        self.posX = 1
        self.posY = 1

    def go(self, direction):
        if direction == "Up":
            self.y -= 1
        elif direction == "Right":
            self.x += 1
        elif direction == "Down":
            self.y += 1
        else:
            self.x -= 1
