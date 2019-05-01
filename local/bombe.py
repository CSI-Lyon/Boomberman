from threading import Thread, RLock
from Image import *
import time
import map

lock = RLock()

class BombPutting(Thread):

    def __init__(self, x, y, canvas, xGridMin, yGridMin):
        Thread.__init__(self)
        self.x = x
        self.y = y
        self.canvas = canvas
        self.xGridMin = xGridMin
        self.yGridMin = yGridMin

    def run(self):
        global scope, mapp
        
        #with lock:
        for i in range(2):
            map.set2(self.y,self.x, 7) #7 : id de la bombe
            bomb = self.canvas.create_image(self.xGridMin + self.x*35 + 35/2 + 1, self.yGridMin + self.y*35 + 35/2 + 1, image = bombe)
            time.sleep(0.2)
            canvas.destroy(bomb)
            bomb2 = self.canvas.create_image(self.xGridMin + self.x*35 + 35/2 + 1, self.yGridMin + self.y*35 + 35/2 + 1, image = bombe)
            time.sleep(0.2)
            print("a")

        canvas.destroy(bomb)
        # Ici, on fait exploser la bombe
        map.set2(self.y,self.x, 0) # On libère la case occupée par la bombe
        #render()
        
        #Haut
        for i in range(self.y-1, self.y-scope-2, -1): #Ici, il faut remplacer scope par player.getScope()
            if i > 0:
                case = map.get2(i, self.x)
                if case != 0 and case != 2:
                    map.set2(i,self.x, 0)
                    break
            else:
                break
        print('e')
        #Droite
        for i in range(self.x+1, self.x+scope+2): #Ici, il faut remplacer scope par player.getScope()
            if i < 5:
                case = map.get2(self.y, i)
                if case != 0 and case != 2:
                    map.set2(self.y,i, 0)
                    break
            else:
                break
        print('e')
        #Bas
        for i in range(self.y+1, self.y+scope+2): #Ici, il faut remplacer scope par player.getScope()
            if i < 5:
                case = map.get2(i, self.x)
                if case != 0 and case != 2:
                    map.set2(self.y,i, 0)
                    break
            else:
                break
        print('e')
        #Gauche
        for i in range(self.x-1, self.x-scope-2, -1): #Ici, il faut remplacer scope par player.getScope()
            if i > 0:
                case = map.get2(self.y, i)
                if case != 0 and case != 2:
                    map.set2(self.y,i, 0)
                    break
            else:
                break
        print('e')

def putBomb(event, player, canvas, xGridMin, yGridMin): #def putBomb(event)
    global scope, bombe, bombe_rouge
    bombe = Image ("objects", "bomb")
    bombe_rouge = Image ("objects", "bomb_rouge")
    scope = 1
    threadBomb = BombPutting(player.posX, player.posY, canvas, xGridMin, yGridMin)
    print("o")
    threadBomb.start()
    print("o")
    threadBomb.join()
    print("o")
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
