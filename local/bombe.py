from threading import Thread, RLock
from Image import *
import time
import map

lock = RLock()

class BombPutting(Thread):
    #initialisation de la bombe
    def __init__(self, x, y, canvas, xGridMin, yGridMin, casesID, player, player2):
        Thread.__init__(self)
        self.x = x
        self.y = y
        self.canvas = canvas
        self.xGridMin = xGridMin
        self.yGridMin = yGridMin
        self.casesID = casesID
        self.player = player
        self.player2 = player2

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
        for i in range(self.y-1, self.y-scope-1, -1):
            if i >= 0:
                try:
                    case = int( map.get2(self.x, i) )
                except:
                    break
                
                #s'il y a un joueur, alors il perd une vie
                if modeGlobal == "multijoueur":
                    if case == 10 and self.player2.ID == 1:
                        self.player2.perdVie()
                        break
                    elif case == 20 and self.player.ID == 2:
                        self.player.perdVie()
                        break
                else:
                    if case == 10:
                        self.player.perdVie()
                    break
                
                #sinon s'il y a un bloc destructible, alors on le détruit

                if case != 0 and case != 2:
                    map.set2(self.x, i, 0)
                    self.canvas.delete(self.casesID[i][self.x])
                    break
                elif case == 0:
                    pass
                else:
                    break
            else:
                break

            
        #Droite
        for i in range(self.x+1, self.x+scope+1): 
            if i <= 18:
                try:
                    case = int( map.get2(i, self.y) )
                except:
                    break
                
                if modeGlobal == "multijoueur":
                    if case == 10 and self.player2.ID == 1:
                        self.player2.perdVie()
                        break
                    elif case == 20 and self.player.ID == 2:
                        self.player.perdVie()
                        break
                else:
                    if case == 10:
                        self.player.perdVie()
                    break
                
                if case != 0 and case != 2:
                    map.set2(i, self.y, 0)
                    self.canvas.delete(self.casesID[self.y][i])
                    break
                elif case == 0:
                    pass
                else:
                    break
            else:
                break

            
        #Bas
        for i in range(self.y+1, self.y+scope+1): 
            if i <= 18:
                try:
                    case = int( map.get2(self.x, i) )
                except:
                    break
                
                if modeGlobal == "multijoueur":
                    if case == 10 and self.player2.ID == 1:
                        self.player2.perdVie()
                        break
                    elif case == 20 and self.player.ID == 2:
                        self.player.perdVie()
                        break
                else:
                    if case == 10:
                        self.player.perdVie()
                    break
                
                if case != 0 and case != 2:
                    map.set2(self.x,i, 0)
                    self.canvas.delete(self.casesID[i][self.x])
                    break
                elif case == 0:
                    pass
                else:
                    break
            else:
                break

            
        #Gauche
        for i in range(self.x-1, self.x-scope-1, -1): 
            if i >= 0:
                case = int( map.get2(i, self.y) )
                print(case)
                if modeGlobal == "multijoueur":
                    if case == 10 and self.player2.ID == 1:
                        self.player2.perdVie()
                        break
                    elif case == 20 and self.player.ID == 2:
                        self.player.perdVie()
                        break
                else:
                    if case == 10:
                        self.player.perdVie()
                    break
                
                if case != 0 and case != 2:
                    map.set2(i, self.y, 0)
                    self.canvas.delete(self.casesID[self.y][i])
                    break
                elif case == 0:
                    pass
                else:
                    break
            else:
                break
    

def putBomb(player,player2, canvas, xGridMin, yGridMin, casesID, mode): 
    global scope, bombe, bombe_rouge, grass, modeGlobal
    #import des images
    bombe = Image ("objects", "bomb")
    bombe_rouge = Image ("objects", "bomb_rouge")
    grass = Image("blocks", "grass")
    scope = 3
    modeGlobal = mode
    #on commence ŕ initialiser la fonction qui fait fonctionner la bombe
    threadBomb = BombPutting(player.posX, player.posY, canvas, xGridMin, yGridMin, casesID, player, player2)
    threadBomb.start()
