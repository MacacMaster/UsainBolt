#-*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import *
import sqlite3
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
        self.barreTaches()

    def barreTaches(self):
        #menu deroulante

        self.menubar = Menu(self.root)
        self.menubar.add_command(label="Enregistrer", command= lambda: self.parent.modele.enregistrer(self.text))
        self.menubar.add_command(label="Charger un fichier", command= lambda: self.parent.modele.explorateurFichiers(self.text))
        self.root.config(menu=self.menubar)
        
    def choisirMot(self,event):
        start = self.text.index('@%s,%s wordstart' % (event.x, event.y))
        stop = self.text.index('@%s,%s wordend' % (event.x, event.y))
        mot = repr(self.text.get(start, stop))
        #pour enlever les guillemets au debut et a la fin du mot
        mot = mot[1:-1]
        return mot
        
    
    def ecranMandat(self):
        self.frameMandat = Frame(self.fenetre, width = self.largeurMandat, height=self.hauteurMandat, bg="steelblue", relief=RAISED, padx=10, pady=10)
        self.frameMandat.pack()
        self.text = Text(self.frameMandat, width=100, height=20)
        texteInitial = self.texteInitial()
        self.text.insert("%d.%d" %(0,1),texteInitial)
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
        self.tfExpression.insert(0, "Cliquer sur un mot")
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
        self.canAnalyse=Canvas(self.frameAnalyse, height=450, bg="light gray")
        self.canAnalyse.pack(fill=X)
        

        #1ere ligne grille
        self.labelVide=Label(self.frameAnalyse, text="", width=100, height=50, bg="white", relief=RAISED )
        self.canAnalyse.create_window(75,40,window=self.labelVide, width=100, height=40)
        self.labelObjet=Label(self.frameAnalyse, text="Objet", width=220, height=50, bg="white",relief=RAISED )
        self.canAnalyse.create_window(235,40,window=self.labelObjet, width=220, height=40)
        self.labelAction=Label(self.frameAnalyse, text="Action", width=220, height=50, bg="white",relief=RAISED )
        self.canAnalyse.create_window(455,40,window=self.labelAction, width=220, height=40)
        self.labelAttribut=Label(self.frameAnalyse, text="Attribut", width=220, height=50, bg="white",relief=RAISED )
        self.canAnalyse.create_window(675,40,window=self.labelAttribut, width=220, height=40)
        
        #2e ligne grille
        self.labelExplicite=Label(self.frameAnalyse, text="Explicite", width=100, height=80, bg="white", relief=RAISED )
        self.canAnalyse.create_window(75,120,window=self.labelExplicite, width=100, height=120)
        self.listExpObj=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(235,120,window=self.listExpObj, width=220, height=120)
        self.listExpAct=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(455,120,window=self.listExpAct, width=220, height=120)
        self.listExpAtt=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(675,120,window=self.listExpAtt, width=220, height=120)
        
        #3e ligne grille
        self.labelImplicite=Label(self.frameAnalyse, text="Implicite", width=100, height=80, bg="white", relief=RAISED )
        self.canAnalyse.create_window(75,240,window=self.labelImplicite, width=100, height=120)
        self.listImpObj=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(235,240,window=self.listImpObj, width=220, height=120)
        self.listImpAct=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(455,240,window=self.listImpAct, width=220, height=120)
        self.listImpAtt=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(675,240,window=self.listImpAtt, width=220, height=120)
        
        
        #4e ligne grille
        self.labelSupplementaire=Label(self.frameAnalyse, text="Supplementaire", width=100, height=80, bg="white", relief=RAISED )
        self.canAnalyse.create_window(75,360,window=self.labelSupplementaire, width=100, height=120)
        self.listSupObj=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(235,360,window=self.listSupObj, width=220, height=120)
        self.listSupAct=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(455,360,window=self.listSupAct, width=220, height=120)
        self.listSupAtt=Listbox(self.frameAnalyse,width=220,height=120)
        self.canAnalyse.create_window(675,360,window=self.listSupAtt, width=220, height=120)
        

    def texteInitial(self):
        conn = sqlite3.connect('donnees.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM mandats')
        texteMandat = c.fetchone()[0]
               
        conn.close()
        return texteMandat
        
              
    def tagging(self,event):
        # get the index of the mouse click
        index = self.text.index("@%s,%s" % (event.x, event.y))
        # get the indices of all "adj" tags
        char = (self.parent.vue.text.get(index))
        if (char != '\n'):
            tag_indices = list(self.text.tag_ranges("jaune"))
            #enlever le tag "jaune" qui se trouve dans l'index choisi
            #index2 = index+1 
            #self.text.tag_remove(str("jaune"),str(index),str(index+1))
             
            self.text.tag_add("jaune", "@%d,%d" % (event.x, event.y))   
            self.propagateTag(event)
            self.specialEffect()
            self.parent.modele.ajouter(self.frameMandat)
            mot = self.choisirMot(event)
            self.tfExpression.delete(0,END)
            self.tfExpression.insert(0,mot)
            
            self.canCommande.create_window(400,30,window=self.tfExpression,width=600,height=20)
        
    def propagateTag(self, event):
        
        start = self.text.index('@%s,%s wordstart' % (event.x, event.y))
        end = self.text.index('@%s,%s wordend' % (event.x, event.y))
        self.text.tag_add("jaune",start, end)    
  
    def specialEffect(self):
        self.text.tag_config('jaune', background='yellow')
  


  
class Modele():
    def __init__(self, parent):
        self.parent=parent
        self.creerTables() # a enlever (tests)

    def ajouter(self,canva):
        self.mots = []
        lesTags = self.parent.vue.text.tag_ranges("jaune")
        temp = ""
        #data = self.text.get("1.0",END)
        avant = 0   
        ranges = self.parent.vue.text.tag_ranges("jaune")        
        for i in range(0, len(ranges), 2):
            start = ranges[i]
            stop = ranges[i+1]
            self.mots.append(( (repr(self.parent.vue.text.get(start, stop))) ))
     
    #tests (a enlever plus tard)        
    def creerTables(sel):
        conn = sqlite3.connect('donnees.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS  mots
                     (mot text)''')
        c.execute('''CREATE TABLE IF NOT EXISTS  mandats
                     (mandat text)''')
        mandat = "<----Regardez les accolades qui sont apparues!---->"
        c.execute('INSERT INTO mandats VALUES(?)', (mandat,) )
        c.execute("select name from sqlite_master where type = 'table'")
        #print(c.fetchall())
        conn.commit()
        conn.close()     
    
    def enregistrer(self,texteMandat):
        #texteMandat = texteMandat.get(1.0,'end-1c')
        texteMandat = texteMandat.get(1.0,'end-1c')
        #print(texteMandat)
        conn = sqlite3.connect('donnees.db')
        c = conn.cursor()
        #pour des fins de tests
        c.execute('''DELETE FROM mandats''')
        c.execute('INSERT INTO mandats VALUES(?)', (texteMandat,))
        conn.commit()
        conn.close()
        
        
            
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








class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
    

        
if __name__ == '__main__':
    c=Controleur()