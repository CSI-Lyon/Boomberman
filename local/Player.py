from Image import *
from threading import Thread
from tkinter import *

import pdb
import time
import map

class Player():

    #initialisation de la classe joueur
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

    #Si on perd une vie
    def pertVie(self):
        global gameOver
        self.vie-=1
        print("vie",self.vie)
        #si 0 vie alors on a perdu
        if self.vie == 0:
            gameOver = PhotoImage(file = "images/decor/game over.png")
            self.canvas.create_image(750, 400, image = gameOver)


class Ennemi(Thread):
    #initialisation de la classe ennemie
    def __init__(self, canvas, imageID, posX, posY, alive, player):
        Thread.__init__(self)
        self.canvas = canvas
        self.imageID = imageID
        self.posX = posX
        self.posY = posY
        self.alive = alive
        self.player = player

    #si un ennemie est mort
    def dele(self):
        global win
        self.canvas.delete(self.imageID)
        self.player.ennemisADetruire-=1
        #s'il n'y a plus d'ennemie et que le joueur a encore au moins une vie, alors il a gagne
        if self.player.ennemisADetruire == 0 and self.player.vie != 0:
            win = PhotoImage(file = "images/decor/winner1.png")
            self.canvas.create_image(750, 400, image = win)

    #ennemie se deplacant ŕ droite
    def droite(self, g):
        #pdb.set_trace()
        
        #tant que l'ennemi peut avancer
        while self.posX < 18 and (int(map.get2(self.posX+1, self.posY)) == 50 \
              or int(map.get2(self.posX+1, self.posY)) == 0\
              or int(map.get2(self.posX+1, self.posY)) == 10\
              or int(map.get2(self.posX+1, self.posY)) == 7):

            print("case", map.get2(self.posX+1, self.posY), self.posX+1, self.posY)

            #si c'est une zone oů il y a un joueur, alors le joueur perd une vie
            if int(map.get2(self.posX+1, self.posY)) == 10:
                self.player.pertVie()

            elif int(map.get2(self.posX+1, self.posY)) == 7:
                self.alive = False
                self.dele()
                return 0

            print("enne", int(map.get2(self.posX+1, self.posY)))

            #si le joueur a perdu, alors on detruit l'ennemie
            if self.player.vie == 0:
                self.alive = False
                self.dele()
                return 0
                    
            #try:
                #si la case suivante est une bombe, alors l'ennemie meurt
            #    caseSuivante = int(map.get2(self.posX+2, self.posY))
            #    if caseSuivante == 7:
            #        self.alive = False
            #except:
            #    pass

            print("droite bouge")

            #si l'ennemie n'est pas sorti de la grille, alors il va avancer vers la droite
            if self.posX < 18:
                self.posX+=1
                for i in range(5):
                    self.canvas.move(self.imageID, +7, 0)
                    time.sleep(0.05)
            else:
                return 0
            
            if self.alive == False:
                #fonction qui détruit le fantome si rentre dans une bombe
                self.dele()
                return 0
       

    def gauche(self,f):
        #tant que l'ennemi peut avancer
        
        while int(map.get2(self.posX-1, self.posY)) == 50 \
              or int(map.get2(self.posX-1, self.posY)) == 0\
              or int(map.get2(self.posX-1, self.posY)) == 10\
              or int(map.get2(self.posX-1, self.posY)) == 7:
            
            print("case", int(map.get2(self.posX+1, self.posY)), self.posX+1, self.posY==7)
        

            #si c'est une zone oů il y a un joueur, alors le joueur perd une vie
            if int(map.get2(self.posX-1, self.posY)) == 10:
                self.player.pertVie()

            elif int(map.get2(self.posX-1, self.posY)) == 7:
                self.alive = False
                self.dele()
                return 0

            print("enne", int(map.get2(self.posX+1, self.posY)))

            #si le joueur a perdu, alors on detruit l'ennemie
            if self.player.vie == 0:
                self.alive = False
                self.dele()
                    
            #try:
            #    #si la case suivante est une bombe, alors l'ennemie meurt
            #    caseSuivante = int(map.get2(self.posX-2, self.posY))
            #    print("case suiv", caseSuivante)
            #    if caseSuivante == 7:
            #        self.alive = False
            #except:
            #    pass


            #si l'ennemie n'est pas sorti de la grille, alors il va avancer
            if self.posX > 1:
                self.posX-=1
                for i in range(5):
                    self.canvas.move(self.imageID, -7, 0)
                    time.sleep(0.05)
            else:
                return 0
            
            
            if self.alive == False:
                #fonction qui détruit le fantome si rentre dans une bombe
                self.dele()
                return 0
    
    def run(self):
        
        while self.alive == True:
            self.gauche(self)
            if self.alive == True:
                self.droite(self)

