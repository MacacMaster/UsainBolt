from tkinter import *

class Controleur():
    def __init__(self):
        self.vue = Vue(self)
        self.modele= Modele(self)
        self.vue.root.mainloop()
    
class Modele():
    def __init__(self, pControleur):
        self.controleur = pControleur
    
class Vue():
    def __init__(self, pControleur):
        self.controleur = pControleur
        self.largeur = 800
        self.hauteur = 600
        self.root = Tk()
        self.fenetre = Frame(self.root, width = self.largeur, height = self.hauteur)
        self.fenetre.pack()
        self.caneva = Canvas(self.fenetre, width = self.largeur, height=self.hauteur, bg="steelblue")
        self.caneva.pack()
        
        labnbe=Label(text="Cas d'usage       ",bg="lightblue")
        self.caneva.create_window(150,80,window=labnbe)
        self.labelCasUsage=Entry(bg="white")
        self.caneva.create_window(300,80,window=self.labelCasUsage,width=150,height=23)
        
        labnbe=Label(text="Action usager    ",bg="lightblue")
        self.caneva.create_window(150,110,window=labnbe)
        self.labelActionUsager=Entry(bg="white")
        self.caneva.create_window(300,110,window=self.labelActionUsager,width=150,height=23)
        
        labnbe=Label(text="Action machine",bg="lightblue")
        self.caneva.create_window(150,140,window=labnbe)
        self.labelActionMachine=Entry(bg="white")
        self.caneva.create_window(300,140,window=self.labelActionMachine,width=150,height=23)
        
if __name__ == '__main__':
    c = Controleur()