from tkinter import *
import time

class Vue():
    def __init__(self, parent):
        self.parent=parent
        self.root=Tk() #Fenetre
        self.root.title("MANDAT")
        self.hauteurTotale=200
        self.largeurTotale=200
        self.hauteurMandat=200
        self.largeurMandat=200
        self.fenetre = Frame(master=self.root, width=self.largeurTotale, height=self.hauteurTotale, bg="steelblue")
        self.fenetre.pack()
        
        
        
        
        self.ecranMandat()
        self.ecranCommande()
        
    def ecranMandat(self):
        self.frameMandat = Frame(self.fenetre, width = self.largeurMandat, height=self.hauteurMandat, bg="steelblue", relief=RAISED, padx=10, pady=10)
        self.frameMandat.pack()
        self.text = Text(self.frameMandat, width=100, height=20)
        self.text.insert("%d.%d" %(0,1),"User-defined marks are named positions in the text. INSERT and CURRENT are predefined marks, but you can also create your own marks. See below for more information.")
        self.text.bind("<Button-1>",self.tagging)
        self.text.pack()
        
        
    def ecranCommande(self):
        self.frameCommande=Frame(self.fenetre, width=self.largeurMandat, height=self.hauteurTotale/2, bg="steelblue", padx=10,pady=10)
        self.frameCommande.pack(fill=X)
        self.canCommande=Canvas(self.frameCommande, height=100, bg="light gray")
        self.canCommande.pack(fill=X)
        #Entree de l'expression
        #self.lblExpression=Label(self.frameCommande, text="Expression:", padx=30, pady=10, bg="light gray")
        #self.lblExpression.pack(side=LEFT)
        self.tfExpression=Entry(self.canCommande, width=100)
        self.canCommande.create_window(400,30,window=self.tfExpression,width=600,height=20)
        
        self.btnObjet=Button(self.frameCommande, text="Objet", width=30)
        self.canCommande.create_window(150,70,window=self.btnObjet,width=110,height=30)
        self.btnAction=Button(self.frameCommande, text="Action", width=30)
        self.canCommande.create_window(275,70,window=self.btnAction,width=110,height=30)
        self.btnAttribut=Button(self.frameCommande, text="Attribut", width=30)
        self.canCommande.create_window(400,70,window=self.btnAttribut,width=110,height=30)
        self.btnImplicite=Button(self.frameCommande, text="Implicite", width=30)
        self.canCommande.create_window(525,70,window=self.btnImplicite,width=110,height=30)
        self.btnSupplementaire=Button(self.frameCommande, text="Supplementaire", width=30)
        self.canCommande.create_window(650,70,window=self.btnSupplementaire,width=110,height=30)
    
    def ecranAnalyse(self):
        pass
     
        
        #Affichage du mandat
    
    
    
    
    
        
    def tagging(self,event):
        # get the index of the mouse click
        index = self.text.index("@%s,%s" % (event.x, event.y))

        # get the indices of all "adj" tags
        tag_indices = list(self.text.tag_ranges("jaune"))
        #enlever le tag "jaune" qui se trouve dans l'index choisi
        #index2 = index+1
        
        #self.text.tag_remove(str("jaune"),str(index),str(index+1))
         
        self.text.tag_add("jaune", "@%d,%d" % (event.x, event.y))   
        self.propagateTag(event)
        self.specialEffect()
        self.ajouter(self.canva)
        self.updateListe()
        
        
  
class Modele():
    def __init__(self, parent):
        self.parent=parent

    
            

class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
    
    
        
if __name__ == '__main__':
    c=Controleur()