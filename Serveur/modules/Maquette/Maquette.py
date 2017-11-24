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
<<<<<<< HEAD
        self.x=0
        self.y=0
        self.x2=0
        self.y2=0
        self.cercle=False;
        self.rect=False;
=======
>>>>>>> 02030141a51a9eca448d5d68a0c293bb06a4f102
      

    
    def menuInitial(self):
<<<<<<< HEAD
        self.caneva = Canvas(self.fenetre, width = self.largeur-200, height=self.hauteur, bg="white")
        self.caneva.pack(side=LEFT)
        self.cadreBtn = Canvas(self.fenetre, width = 200, height=self.hauteur, bg="white")
        self.cadreBtn.pack(side=LEFT)
        
        self.btnRectangle=Button(self.cadreBtn,text="Rectangle",width=30,command=self.creeRectangle())
        self.cadreBtn.create_window(100,100,window=self.btnRectangle,width=150,height=30)
    
        self.btnCercle=Button(self.cadreBtn,text="Cercle",width=30,command=self.creeCercle())
        self.cadreBtn.create_window(100,250,window=self.btnCercle,width=150,height=30)
        
        self.bntTexte=Button(self.cadreBtn,text="Texte",width=30)#
        self.cadreBtn.create_window(100,200,window=self.bntTexte,width=150,height=30)
        
        self.bntFleche=Button(self.cadreBtn,text="Fleche",width=30)
        self.cadreBtn.create_window(100,300,window=self.bntFleche,width=150,height=30)

        self.btnRectangle=Button(self.cadreBtn,text="Commit",width=30)
        self.cadreBtn.create_window(100,500,window=self.btnRectangle,width=150,height=30)
    
        self.btnCercle=Button(self.cadreBtn,text="Supprimer",width=30)
        
        self.cadreBtn.create_window(100,550,window=self.btnCercle,width=150,height=30)
        self.caneva.bind('<B1-Motion>', self.bouge)
        self.caneva.pack(padx =5, pady =5)
        
        self.caneva.bind('<B1-Motion>', self.bouge)
        self.caneva.pack(padx =5, pady =5)
        
        self.caneva.bind('<Button-1>', self.clic)
        self.caneva.pack(padx =5, pady =5)
       
        self.caneva.bind('ButtonRelease-1', self.release)
        self.caneva.pack(padx =5, pady =5)
    
    def bouge(self,event):
        self.x2 = event.x
        self.y2 = event.y
        print(self.x2,self.y2)
        self.dessinerTempo()
    
    def clic(self,event):
        self.x = event.x
        self.y = event.y
        print(self.x,self.y)

    def release(self):
        self.x2 = event.x
        self.y2 = event.y
        self.dessiner()
    
    def creeCercle(self):
        self.cercle=True;
   
    def creeRectangle(self):
        self.rect=True
                    
    def detruitTempo(self):
       pass

        
    def dessinerTempo(self):
        if(self.cercle):
            self.caneva.create_oval(self.x,self.y,self.x+self.x,self.y+self.x,tags="Forme")
        
        self.caneva.create_rectangle(self.x,self.y,self.x2,self.y2,tags="Forme")
        self.caneva.delete("Forme")
      
 
=======
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

            
           
         
            

>>>>>>> 02030141a51a9eca448d5d68a0c293bb06a4f102
               

if __name__ == '__main__':
    c = Controleur()