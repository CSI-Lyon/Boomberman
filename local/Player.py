from Image import *
from threading import Thread
from tkinter import *

import pdb
import time
import map

class Player():

    #initialisation de la classe joueur
    def __init__(self, ID, name, imageID, posX, posY, ennemisADetruire, canvas, textVieID, vie):
        self.ID = ID
        self.name = name
       
        self.imageID = imageID
        self.posX = posX
        self.posY = posY

        self.vie = vie
        self.ennemisADetruire = ennemisADetruire
        self.canvas = canvas
        self.textVieID = textVieID

    #Si on perd une vie
    def perdVie(self):
        global gameOver
        self.vie-=1
        print("vie",self.vie)
        if self.vie >= 0:
            self.canvas.itemconfig(self.textVieID, text = str(self.vie))
        #si 0 vie alors on a perdu
        if self.vie == 0:
            gameOver = PhotoImage(file = "images/decor/game over.png")
            self.canvas.create_image(750, 400, image = gameOver)
            self.canvas.delete(self.IDimage)

    def move(self, key):
        global imgJ1, imgJ2

        case = -1
        if self.ID == 1:
            imgJ1 = PhotoImage (file = "images/skins/1/down.png")
            self.canvas.itemconfig(self.IDimage, image = imgJ1)
        elif self.ID == 2:
            imgJ2 = PhotoImage (file = "images/skins/2/down.png")
            self.canvas.itemconfig(self.IDimage, image = imgJ2)

        #si l'utilisateur appuie sur la touche de haut
        if key == "Up" and self.posY >= 1:
            case = map.get2(self.posX, self.posY-1)
            if int(case) == 0 or int(case) == 50:
                #s'il y a un fantome (ennemi), alors il perd une vie
                if int(case) == 50:
                    self.vie-=1

                if self.ID == 1:
                    imgJ1 = PhotoImage (file = "images/skins/1/up.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ1)
                elif self.ID == 2:
                    imgJ2 = PhotoImage (file = "images/skins/2/up.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ2)
                #on le fait bouger
                self.canvas.move(self.IDimage, 0, -35)
                self.posY -= 1
                #on remplace les bons ID pour chaque case
                if self.ID == 1:
                    if map.get2(self.posX, self.posY+1) == 10:
                        map.set2(self.posX, self.posY+1, 0)
                    map.set2(self.posX, self.posY, 10)
                elif self.ID == 2:
                    if map.get2(self.posX, self.posY+1) == 20:
                        map.set2(self.posX, self.posY+1, 0)
                    map.set2(self.posX, self.posY, 20)

        #
        #   Pour bas, droite et gauche, męme fonctinonement que celui de la touche en haut
        #
        
        elif key == "Down" and self.posY <= 9:
            case = map.get2(self.posX, self.posY+1)
            if int(case) == 0 or int(case) == 50:
                if int(case) == 50:
                    self.vie-=1
                    
                if self.ID == 1:
                    imgJ1 = PhotoImage (file = "images/skins/1/down.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ1)
                elif self.ID == 2:
                    imgJ2 = PhotoImage (file = "images/skins/2/down.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ2)

                self.canvas.move(self.IDimage, 0, +35)
                self.posY += 1
                if self.ID == 1:
                    if map.get2(self.posX, self.posY-1) == 10:
                        map.set2(self.posX, self.posY-1, 0)
                    map.set2(self.posX, self.posY, 10)
                elif self.ID == 2:
                    if map.get2(self.posX, self.posY-1) == 20:
                        map.set2(self.posX, self.posY-1, 0)
                    map.set2(self.posX, self.posY, 20)
            
        elif key == "Right" and self.posX <= 17:
            case = map.get2(self.posX+1, self.posY)
            if int(case) == 0 or int(case) == 50:
                if int(case) == 50:
                    self.vie-=1
                    
                if self.ID == 1:
                    imgJ1 = PhotoImage (file = "images/skins/1/right.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ1)
                elif self.ID == 2:
                    imgJ2 = PhotoImage (file = "images/skins/2/right.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ2)

                self.canvas.move(self.IDimage, +35, 0)
                self.posX += 1
                if self.ID == 1:
                    if map.get2(self.posX-1, self.posY) == 10:
                        map.set2(self.posX-1, self.posY, 0)
                    map.set2(self.posX, self.posY, 10)
                elif self.ID == 2:
                    if map.get2(self.posX-1, self.posY) == 20:
                        map.set2(self.posX-1, self.posY, 0)
                    map.set2(self.posX, self.posY, 20)
        
        elif key == "Left" and self.posX >= 1:
            case = map.get2(self.posX-1, self.posY)
            if int(case) == 0 or int(case) == 50:
                if int(case) == 50:
                    self.vie-=1
                    
                if self.ID == 1:
                    imgJ1 = PhotoImage (file = "images/skins/1/left.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ1)
                elif self.ID == 2:
                    imgJ2 = PhotoImage (file = "images/skins/2/left.png")
                    self.canvas.itemconfig(self.IDimage, image = imgJ2)

                self.canvas.move(self.IDimage, -35, 0)
                self.posX -= 1
                if self.ID == 1:
                    if map.get2(self.posX+1, self.posY) == 10:
                        map.set2(self.posX+1, self.posY, 0)
                    map.set2(self.posX, self.posY, 10)
                elif self.ID == 2:
                    print(self.posX+1, self.posY)
                    if map.get2(self.posX+1, self.posY) == 20:
                        map.set2(self.posX+1, self.posY, 0)
                    map.set2(self.posX, self.posY, 20)


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
        
        #tant que l'ennemi peut avancer
        while self.posX < 18 and (int(map.get2(self.posX+1, self.posY)) == 50 \
              or int(map.get2(self.posX+1, self.posY)) == 0\
              or int(map.get2(self.posX+1, self.posY)) == 10\
              or int(map.get2(self.posX+1, self.posY)) == 7):

            
            #si c'est une zone oů il y a un joueur, alors le joueur perd une vie
            if int(map.get2(self.posX+1, self.posY)) == 10:
                self.player.perdVie()

            if int(map.get2(self.posX+1, self.posY)) == 7:
                self.alive = False
                self.dele()
                return 0

            #si le joueur a perdu, alors on detruit l'ennemie
            if self.player.vie == 0:
                self.alive = False
                self.dele()
                return 0
                    
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
            
            #print("case", int(map.get2(self.posX+1, self.posY)), self.posX+1, self.posY==7)
        

            #si c'est une zone oů il y a un joueur, alors le joueur perd une vie
            if int(map.get2(self.posX-1, self.posY)) == 10:
                self.player.perdVie()

            if int(map.get2(self.posX-1, self.posY)) == 7:
                self.alive = False
                self.dele()
                return 0

            #si le joueur a perdu, alors on detruit l'ennemie
            if self.player.vie == 0:
                self.alive = False
                self.dele()
                    

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

