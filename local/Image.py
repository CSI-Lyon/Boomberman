from tkinter import PhotoImage

#classe image
class Image(PhotoImage):
    
    #définition de la classe
    def __init__(self, directory, name):
        self.type = directory
        #ouvrir une image à partir de d'un modèle : dossier et nom
        PhotoImage.__init__(self, file="images/{}/{}.png".format(self.type, name))
        self.ID = PhotoImage._last_id
