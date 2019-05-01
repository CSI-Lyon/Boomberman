from tkinter import PhotoImage

class Image(PhotoImage):

    def __init__(self, directory, name):
        self.type = directory

        PhotoImage.__init__(self, file="images/{}/{}.png".format(self.type, name))
        self.ID = PhotoImage._last_id

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def getID(self):
        return self.ID
