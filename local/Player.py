from Image import *
from threading import Thread
from tkinter import *

import time
import map

#def dele(canvas, imageID):
#    print(imageID)
#    canvas.destroy(imageID)

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
    def __init__(self, canvas, imageID, posX, posY, alive):
        Thread.__init__(self)
        self.canvas = canvas
        self.imageID = imageID
        self.posX = posX
        self.posY = posY
        self.alive = alive

    def droite(self, g):
        while int(map.get2(self.posX+1, self.posY)) == 50 or int(map.get2(self.posX+1, self.posY)) == 0:
            print("ghost_droite>>>>>>")
            for i in range(5):
                self.canvas.move(self.imageID, 7, 0)
                time.sleep(0.1)

            print("droite : ",self.posX)
            if self.posX < 17:
                self.posX+=1
            else:
                return 0
            
        if self.alive == False:
            return 0
       

    def gauche(self,f):
        while int(map.get2(self.posX-1, self.posY)) == 50 or int(map.get2(self.posX-1, self.posY)) == 0:
            #self.posX-=1
            print(self, self.posX)
            for i in range(5):
                self.canvas.move(self.imageID, -7, 0)
                time.sleep(0.1)
                
            caseSuivant = int(map.get2(self.posX-2, self.posY))
            if caseSuivant == 7:
                self.alive = False
            #    return 0
            print("gauche : ",self.posX)
            if self.posX > 1:
                self.posX-=1
            else:
                return 0
            
        if self.alive == False:
            #fonction qui détruit le fantome si rentre dans une bombe
            #dele(self.canvas, self.imageID)
            return 0
        print("fini")

    def run(self):
        
        while self.alive == True:
            self.gauche(self)
            if self.alive == True:
                self.droite(self)
