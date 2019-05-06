from Image import *
from threading import Thread
from tkinter import *

import time
import map

class Player():

    def __init__(self, ID, name, imageID, posX, posY, ennemisADetruire, canvas):
        self.ID = ID
        self.name = name
       
        self.imageID = imageID
        self.posX = posX
        self.posY = posY

        self.nbBombs = 1
        self.vie = 2
        self.ennemisADetruire = ennemisADetruire
        self.canvas = canvas

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def pertVie(self):
        global gameOver
        self.vie-=1
        print("vie",self.vie)
        if self.vie == 0:
            gameOver = PhotoImage(file = "images/decor/game over.png")
            self.canvas.create_image(750, 400, image = gameOver)


class Ennemi(Thread):
    def __init__(self, canvas, imageID, posX, posY, alive, player):
        Thread.__init__(self)
        self.canvas = canvas
        self.imageID = imageID
        self.posX = posX
        self.posY = posY
        self.alive = alive
        self.player = player

    def dele(self):
        global win
        self.canvas.delete(self.imageID)
        self.player.ennemisADetruire-=1
        if self.player.ennemisADetruire == 0 and self.player.vie != 0:
            win = PhotoImage(file = "images/decor/winner1.png")
            self.canvas.create_image(750, 400, image = win)

    def droite(self, g):
        while int(map.get2(self.posX+1, self.posY)) == 50 \
              or int(map.get2(self.posX+1, self.posY)) == 0\
              or int(map.get2(self.posX+1, self.posY)) == 10:
            
            if int(map.get2(self.posX+1, self.posY)) == 10:
                self.player.pertVie()
            if self.player.vie == 0:
                self.alive = False

            if self.posX < 17:
                self.posX+=1
                for i in range(5):
                    self.canvas.move(self.imageID, 7, 0)
                    time.sleep(0.05)
            else:
                return 0
            

            try:
                caseSuivant = int(map.get2(self.posX+2, self.posY))
                if caseSuivant == 7:
                    self.alive = False
            except:
                pass

            
            
        if self.alive == False:
            self.dele()
            return 0
       

    def gauche(self,f):
        while int(map.get2(self.posX-1, self.posY)) == 50 \
              or int(map.get2(self.posX-1, self.posY)) == 0\
              or int(map.get2(self.posX-1, self.posY)) == 10:

            if int(map.get2(self.posX-1, self.posY)) == 10:
                self.player.pertVie()
                
            if self.player.vie == 0:
                self.alive = False
                    
            if self.posX > 1:
                self.posX-=1
                for i in range(5):
                    self.canvas.move(self.imageID, -7, 0)
                    time.sleep(0.05)
            else:
                return 0
            
            try:
                caseSuivant = int(map.get2(self.posX-2, self.posY))
                if caseSuivant == 7:
                    self.alive = False
            except:
                pass
            #    return 0
            print("gauche : ",self.posX)
            
            
        if self.alive == False:
            #fonction qui détruit le fantome si rentre dans une bombe
            self.dele()
            return 0
    
    def run(self):
        
        while self.alive == True:
            self.gauche(self)
            if self.alive == True:
                self.droite(self)
