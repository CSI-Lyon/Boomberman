from Image import *
from threading import Thread
import time
import map

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

class Ennemi(Thread):
    def __init__(self, imageID, posX, posY, alive):
        Thread.__init__(self)
        self.imageID = imageID
        self.posX = posX
        self.posY = posY
        self.alive = alive

    def droite(self, g):
        while (map.get2(self.posX, self.posY) == 0 or map.get2(self.posX, self.posY) == 50):
            for i in range(5):
                canvas.move(self.imageID, 7, 0)
                time.sleep(1)
            posX+=1
        if self.alive == False:
            return 0

    def gauche(self,f):
        while (map.get2(self.posX, self.posY) == 0 or map.get2(self.posX, self.posY) == 50):
            for i in range(5):
                canvas.move(self.imageID, -7, 0)
                time.sleep(1)
            posX-=1
        if self.alive == False:
            return 0

    def run(self):
        while self.alive == True:
            self.gauche(self)
            self.droite(self)

        
