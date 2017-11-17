from tkinter import *
from tkinter.filedialog import *
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
        self.text = ""
                
        
        self.ecranMandat()
        self.ecranCommande()
        
        self.ecranAnalyse()
        #self.explorateurFichiers(self.text) 
               
        #menu deroulante
        menubar = Menu(self.root)
        self.filemenu = Menu(menubar, tearoff=0)
        #self.filemenu.add_command(label="Enregistrer", command=hello)
        #self.filemenu.add_command(label="Charger un fichier", command=hello)

        
    def ecranMandat(self):
        self.frameMandat = Frame(self.fenetre, width = self.largeurMandat, height=self.hauteurMandat, bg="steelblue", relief=RAISED, padx=10, pady=10)
        self.frameMandat.pack()
        self.text = Text(self.frameMandat, width=100, height=20)
        self.text.insert("%d.%d" %(0,1),"Texte par defaut du mandat")
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
        self.frameAnalyse=Frame(self.fenetre, width=self.largeurMandat, height=self.hauteurTotale/2, bg="steelblue", padx=10,pady=10)
        self.frameAnalyse.pack(fill=X)
        self.canAnalyse=Canvas(self.frameAnalyse, height=500, bg="light gray")
        self.canAnalyse.pack(fill=X)
        
        #1ere ligne grille
        self.labelVide=Label(self.frameAnalyse, text="Supplementaire", width=100, height=50, bg="white", relief=RAISED )
        self.canAnalyse.create_window(75,40,window=self.labelVide, width=100, height=40)
        self.labelObjet=Label(self.frameAnalyse, text="Objet", width=220, height=50, bg="white",relief=RAISED )
        self.canAnalyse.create_window(235,40,window=self.labelObjet, width=220, height=40)
        self.labelAction=Label(self.frameAnalyse, text="Action", width=220, height=50, bg="white",relief=RAISED )
        self.canAnalyse.create_window(455,40,window=self.labelAction, width=220, height=40)
        self.labelAttribut=Label(self.frameAnalyse, text="Attribut", width=220, height=50, bg="white",relief=RAISED )
        self.canAnalyse.create_window(675,40,window=self.labelAttribut, width=220, height=40)
        
        #2e ligne grille
        
        #3e ligne grille
        
        
        
    
    def explorateurFichiers(self,text):
        #ouvrir un fichier
        # filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
        fonctionne = True
        filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt')])
        try:
            fichier = open(filename, "r")
        except FileNotFoundError:
            fonctionne = False
            print("Aucun fichier choisi!")
        if fonctionne:  
            content = fichier.read()
            fichier.close()
            text.insert("%d.%d" %(1,0),content)
        
                        
    def tagging(self,event):
        # get the index of the mouse click
        index = self.text.index("@%s,%s" % (event.x, event.y))

        # get the indices of all "adj" tags
        tag_indices = list(self.text.tag_ranges("jaune"))
        #enlever le tag "jaune" qui se trouve dans l'index choisi
        #index2 = index+1
        
        #self.text.tag_remove(str("jaune"),str(index),str(index+1))
         
        self.text.tag_add("jaune", "@%d,%d" % (event.x, event.y))   
        #self.propagateTag(event)
        self.specialEffect()
        self.parent.modele.ajouter(self.frameMandat)
        
    def propagateTag(self, event):
        start = self.text.index('@%s,%s wordstart' % (event.x, event.y))
        end = self.text.index('@%s,%s wordend' % (event.x, event.y))
        self.text.tag_add("jaune",start, end)    
  
    def specialEffect(self):
        self.text.tag_config('jaune', background='yellow')
  
  
  
  

class Modele():
    def __init__(self, parent):
        self.parent=parent

    def ajouter(self,canva):
        self.mots = []
        lesTags = self.parent.vue.text.tag_ranges("jaune")
        temp = ""
        #data = self.text.get("1.0",END)
        avant = 0 
    
        '''
        ranges = self.text.tag_ranges("jaune")
        for i in range(0, len(ranges), 2):
            start = ranges[i]
            stop = ranges[i+1]
            if (repr(self.text.get(start, stop))) != " ":
                temp += (repr(self.text.get(start, stop)))
            else:
                self.mots += temp
                temp = ""
        '''    
        ranges = self.parent.vue.text.tag_ranges("jaune")        
        for i in range(0, len(ranges), 2):
            start = ranges[i]
            stop = ranges[i+1]
            self.mots.append(( (repr(self.parent.vue.text.get(start, stop))) ))
    
            

class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
    

        
if __name__ == '__main__':
    c=Controleur()