from threading import Thread, RLock
from Image import *
import time
import map

lock = RLock()

class BombPutting(Thread):
    #initialisation de la bombe
    def __init__(self, x, y, canvas, xGridMin, yGridMin, casesID):
        Thread.__init__(self)
        self.x = x
        self.y = y
        self.canvas = canvas
        self.xGridMin = xGridMin
        self.yGridMin = yGridMin
        self.casesID = casesID

    def run(self):
        global scope, mapp

        IDs = []
        #with lock:
        map.set2(self.x,self.y, 7) #7 : id de la bombe
        for i in range(2):
            #on affiche : (terre puis bombe puis terre puis bombe rouge) fois 2
            IDs.append(self.canvas.create_image(self.xGridMin + self.x*35 + 35/2 + 1, self.yGridMin + self.y*35 + 35/2 + 1, image = grass))
            IDs.append(self.canvas.create_image(self.xGridMin + self.x*35 + 35/2 + 1, self.yGridMin + self.y*35 + 35/2 + 1, image = bombe))
            time.sleep(1)
            IDs.append(self.canvas.create_image(self.xGridMin + self.x*35 + 35/2 + 1, self.yGridMin + self.y*35 + 35/2 + 1, image = grass))
            IDs.append(self.canvas.create_image(self.xGridMin + self.x*35 + 35/2 + 1, self.yGridMin + self.y*35 + 35/2 + 1, image = bombe_rouge))
            time.sleep(1)

        IDs.append(self.canvas.create_image(self.xGridMin + self.x*35 + 35/2 + 1, self.yGridMin + self.y*35 + 35/2 + 1, image = grass))
        #on détruit tous les blocs affichés
        for i in IDs:
            for e in range (9):
                self.canvas.delete(i)
                
        # Ici, on fait exploser la bombe
        map.set2(self.x,self.y, 0) # On libère la case occupée par la bombe
        
        #Haut
        for i in range(self.y-1, self.y-scope-2, -1): #Ici, il faut remplacer scope par player.getScope()
            if i >= 0:
                case = int( map.get2(self.x, i) )
                if case != 0 and case != 2:
                    map.set2(self.x, i, 0)
                    self.canvas.delete(self.casesID[i][self.x])
                    break
                else:
                    break
            else:
                break
        #Droite
        for i in range(self.x+1, self.x+scope+2): #Ici, il faut remplacer scope par player.getScope()
            if i <= 18:
                case = int( map.get2(i, self.y) )
                if case != 0 and case != 2:
                    map.set2(i, self.y, 0)
                    self.canvas.delete(self.casesID[self.y][i])
                    break
                else:
                    break
            else:
                break
        #Bas
        for i in range(self.y+1, self.y+scope+2): #Ici, il faut remplacer scope par player.getScope()
            if i <= 18:
                case = int( map.get2(self.x, i) )
                if case != 0 and case != 2:
                    map.set2(self.x,i, 0)
                    self.canvas.delete(self.casesID[i][self.x])
                    break
                else:
                    break
            else:
                break
        #Gauche
        for i in range(self.x-1, self.x-scope-2, -1): #Ici, il faut remplacer scope par player.getScope()
            if i >= 0:
                case = int( map.get2(i, self.y) )
                if case != 0 and case != 2:
                    map.set2(i, self.y, 0)
                    self.canvas.delete(self.casesID[self.y][i])
                    break
                else:
                    break
            else:
                break
    

def putBomb(event, player, canvas, xGridMin, yGridMin, casesID): #def putBomb(event)
    global scope, bombe, bombe_rouge, grass
    #import des images
    bombe = Image ("objects", "bomb")
    bombe_rouge = Image ("objects", "bomb_rouge")
    grass = Image("blocks", "grass")
    scope = 1
    #on commence ŕ initialiser la fonction qui fait fonctionner la bombe
    threadBomb = BombPutting(player.posX, player.posY, canvas, xGridMin, yGridMin, casesID)
    threadBomb.start()
