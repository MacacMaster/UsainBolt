from tkinter import *

class Controleur():
    def __init__(self):
        self.vue = Vue(self)
        self.unReprend=False
        self.vue.root.mainloop()
        print("controleur")
    
class Vue():
    def __init__(self, pControleur):
        self.controleur = pControleur
        self.largeur = 800
        self.hauteur = 600
        self.root = Tk()
        self.fenetre = Frame(self.root, width = self.largeur, height = self.hauteur)
        self.fenetre.pack()
        self.listeCas=[]
        self.listeEtat=[]
        self.dejaOuvert=False
        self.indiceCasModifier=0
        self.menuInitial()
      

    
    def menuInitial(self):
        self.caneva = Canvas(self.fenetre, width = self.largeur, height=self.hauteur, bg="white")
        self.caneva.pack()
        
        self.btnRectangle=Button(self.caneva,text="Rectangle",width=30)
        self.caneva.create_window(700,100,window=self.btnRectangle,width=150,height=30)
    
        self.btnCercle=Button(self.caneva,text="Cercle",width=30)
        self.caneva.create_window(700,550,window=self.btnCercle,width=150,height=30)
        
        self.bntTexte=Button(self.caneva,text="Texte",width=30)#
        self.caneva.create_window(700,200,window=self.bntTexte,width=150,height=30)
        
        self.bntFleche=Button(self.caneva,text="Fleche",width=30)
        self.caneva.create_window(700,300,window=self.bntFleche,width=150,height=30)

      
        
        self.btnRectangle=Button(self.caneva,text="Commit",width=30)
        self.caneva.create_window(700,500,window=self.btnRectangle,width=150,height=30)
    
        self.btnCercle=Button(self.caneva,text="Supprimer",width=30)
        self.caneva.create_window(700,550,window=self.btnCercle,width=150,height=30)
        
    def callback(event):
        print ("clicked at", event.x, event.y)

            
           
         
            

               

if __name__ == '__main__':
    c = Controleur()