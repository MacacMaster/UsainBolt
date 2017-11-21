from tkinter import *
from logging.config import listen

class Controleur():
    def __init__(self):
        self.vue = Vue(self)
        self.modele= Modele(self)
        self.vue.root.mainloop()
        print("controleur")
    
    
    

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
        self.menuInitial()
          
    def ajouterTable(self):
        pass
    
    def entrerTable(self):
        pass
    
    def menuInitial(self):
        
        self.caneva = Canvas(self.fenetre, width = self.largeur, height=self.hauteur, bg="steelblue")
        self.caneva.pack()
        
        self.lblListeTable=Label(text="Liste des tables : ",bg="lightblue")
        self.caneva.create_window(200,90,window=self.lblListeTable)
        
        self.listBoxNomTable=Listbox(self.caneva,bg="lightblue",borderwidth=0,relief=FLAT,width=75,height=20)
        self.caneva.create_window(390,270,window=self.listBoxNomTable)
        
        self.btnAjouterTable=Button(self.caneva,text="Ajouter une table",width=20,command=self.ajouterTable)
        self.caneva.create_window(200,550,window=self.btnAjouterTable,width=150,height=20)
        
        self.btnEntrerTable=Button(self.caneva,text="Ajouter une table",width=20,command=self.entrerTable)
        self.caneva.create_window(600,550,window=self.btnEntrerTable,width=150,height=20)
        
    
if __name__ == '__main__':
    c = Controleur()