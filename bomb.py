from threading import Thread, RLock
from main import *
import time

lock = RLock()

class BombPutting(Thread):

    def __init__(self, x, y):
        Thread.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        global mapp, scope
        
        with lock:
            for i in range(4):
                mapp[self.y][self.x] = 3
                #render()
                time.sleep(0.2)
                mapp[self.y][self.x] = 4
                #render()

        # Ici, on fait exploser la bombe
        mapp[self.y][self.x] = 0 # On libère la case occupée par la bombe
        #render()
        
        #Haut
        for i in range(self.y-1, self.y-scope-2, -1): #Ici, il faut remplacer scope par player.getScope()
            if i > 0:
                case = mapp[i][self.x]
                if case != 0 and case != 2:
                    mapp[i][self.x] = 0
                    break
            else:
                break

        #Droite
        for i in range(self.x+1, self.x+scope+2): #Ici, il faut remplacer scope par player.getScope()
            if i < 5:
                case = mapp[self.y][i]
                if case != 0 and case != 2:
                    mapp[self.y][i] = 0
                    break
            else:
                break

        #Bas
        for i in range(self.y+1, self.y+scope+2): #Ici, il faut remplacer scope par player.getScope()
            if i < 5:
                if case != 0 and case != 2:
                    ase = mapp[i][self.x]
                    mapp[i][self.x] = 0
                    break
            else:
                break

        #Gauche
        for i in range(self.x-1, self.x-scope-2, -1): #Ici, il faut remplacer scope par player.getScope()
            if i > 0:
                case = mapp[self.y][i]
                if case != 0 and case != 2:
                    mapp[self.y][i] = 0
                    break
            else:
                break

def putBomb(event): #def putBomb(event)
    threadBomb = BombPutting(Personnage1.positionX, Personnage1.positionX)
    
    threadBomb.start()

    threadBomb.join()
"""
def main():
    global mapp
    mapp = [
        [1, 1, 1, 0, 0],
        [0, 0, 2, 2, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 2, 2, 1, 0]
    ] # 0 = case vide, 1 = bloc cassable, 2 = bloc incassable, 3 = bombe noire, 4 = bombe rouge (allumée)

    global scope
    scope = 1 # Portée de la bombe

    # Ici on récupère les cordonnées du joueur quand il pose la bombe
    y = 3
    x = 2

    putBomb(x, y)

main()
"""
