from Image import *
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

    def go(self, direction, canvas):
        if direction == "Up" and self.posY >= 1:
            case = map.get2(self.posX, self.posY-1)
            if int(case) == 0 or int(case) == 10:
                canvas.move(self.IDimage, 0, -35)
                self.posY -= 1

        elif direction == "Down" and self.posY <= 9:
            case = map.get2(self.posX, self.posY+1)
            if int(case) == 0 or int(case) == 10:
                canvas.move(self.IDimage, 0, +35)
                self.posY += 1
            
        elif direction == "Right" and self.posX <= 17:
            case = map.get2(self.posX+1, self.posY)
            if int(case) == 0 or int(case) == 10:
                canvas.move(self.IDimage, +35, 0)
                self.posX += 1
        
        elif direction == "Left" and self.posX >= 1:
            case = map.get2(self.posX-1, self.posY)
            if int(case) == 0 or int(case) == 10:
                canvas.move(self.IDimage, -35, 0)
                self.posX -= 1
