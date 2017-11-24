#-*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import *
import sqlite3
import time
from _overlapped import NULL

class Vue():
    def __init__(self, parent):
        self.parent=parent
        self.root=Tk() #Fenetre
        self.root.title("MODULE CRC")
        self.hauteurTotale=200
        self.largeurTotale=200
        self.hauteurMandat=200
        self.largeurMandat=200
        self.fenetre = Frame(master=self.root, width=self.largeurTotale, height=self.hauteurTotale, bg="steelblue")
        self.fenetre.pack()
        self.creerVueMenu()
        
    
    def creerVueMenu(self):  
        self.menu = Frame(self.fenetre, width = self.largeurMandat, height=self.hauteurMandat, bg="steelblue", relief=RAISED, padx=10, pady=10)
        self.menu.pack(side=LEFT)
        #self.menu.pack_propagate(0)
        self.creerMenuGauche()
        self.creerMenuDroite()
        
    def creerMenuGauche(self):
        self.menuGauche = Frame(self.menu, width = self.largeurMandat, height=self.hauteurMandat, bg="steelblue", relief=RAISED, padx=10, pady=10)
        self.menuGauche.pack(side=LEFT)
        
        largeur = 25
        
        frame1 = Frame(self.menuGauche)
        frame1.pack(fill=X, pady=5)
        
        lbl1 = Label(frame1, text="Liste des classes", width=largeur)
        lbl1.pack(side=LEFT, padx=55, pady=5)           
       
        frame2 = Frame(self.menuGauche)
        frame2.pack()
        
        #scrollbar
                
        listeClasses = Listbox(self.menuGauche, height=25)
        listeClasses.pack(fill="y")
        
        scrollbar = Scrollbar(frame2, orient = "vertical")
        scrollbar.config(command=listeClasses.yview)  
        scrollbar.pack(side=RIGHT, fill="y")

        
        listeClasses.config(yscrollcommand=scrollbar.set)
          
        for x in range(30):
            listeClasses.insert(END, str(x))

        
        frame3 = Frame(self.menuGauche)
        frame3.pack(fill=BOTH, expand=True, pady = 5)
        
        btnSuppression = Button(self.menuGauche, text = "Suppression")
        btnSuppression.pack()
        
    
    def creerMenuDroite(self):
        self.menuDroite = Frame(self.menu, width = self.largeurMandat, height=self.hauteurMandat, bg="steelblue", relief=RAISED, padx=10, pady=10)
        self.menuDroite.pack(side=LEFT)
        
        largeur = 25
        
        frame1 = Frame(self.menuDroite)
        frame1.pack(fill=X, pady=5)
        
        lblTitre = Label(frame1, text="Informations", width=largeur)
        lblTitre.pack(side=LEFT, padx=55, pady=5)           
       
        frame2 = Frame(self.menuDroite)
        frame2.pack(fill=X)
        
        lblNomClasse = Label(frame2, text = "nom de la classe")
        lblNomClasse.pack()
        
        lblProprietaire = Label(frame2, text = "propriétaire de la classe")
        lblProprietaire.pack()
        
        lblResponsabilites = Label(frame2, text = "Responsabilités")
        lblResponsabilites.pack()
        
        listeResponsabilites = Listbox(frame2)
        listeResponsabilites.pack()
              
        lblCollaboration = Label(frame2, text = "Collaboration")
        lblCollaboration.pack()
        
        listeCollaboration = Listbox(frame2)
        listeCollaboration.pack()
        
        frame3 = Frame(self.menuDroite)
        frame3.pack(fill=BOTH, expand=True, pady = 5)
        
        btnModification = Button(self.menuDroite, text = "Modification", command=self.creerMenuAjout)
        btnModification.pack()
        
    def creerMenuAjout(self):
        #enlever la premiere fenetre
        self.menuDroite.pack_forget()
        self.menuGauche.pack_forget()
        
        self.menuAjout = Frame(self.menu, width = self.largeurMandat, height=self.hauteurMandat, bg="steelblue", relief=RAISED, padx=10, pady=10)
        self.menuAjout.pack()
        frame1 = Frame(self.menuAjout)
        frame1.pack(fill=X, pady=5)
        
        lblNomClasse = Label(frame1, text="Nom (classe)", width=25)
        lblNomClasse.pack(side=LEFT)  
        
        entryNomClasse = Entry(frame1, text="erer", width=25)
        entryNomClasse.pack(side=LEFT)
        entryNomClasse.insert();
    
class Modele():
    def __init__(self, parent):
        self.parent=parent

    def ajoutListe(self):
        pass
       
    def enregistrer(self,texteMandat):
        #texteMandat = texteMandat.get(1.0,'end-1c')
        texteMandat = texteMandat.get(1.0,'end-1c')
        #print(texteMandat)
        conn = sqlite3.connect('BDD.sqlite')
        c = conn.cursor()
        #pour des fins de tests
        c.execute('''DELETE FROM mandats''')
        c.execute('INSERT INTO mandats VALUES(?)', (texteMandat,))
        conn.commit()
        conn.close()
 
    def insertionSQL(self):  
        pass
        
    def lectureSQL(self):
        pass

class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        #self.serveur = self.connectionServeur()
        self.vue=Vue(self)
        self.vue.root.mainloop()
    
    def connectionServeur(self):
        ad="http://"+pUsagerIP+":9998"
        print("Connection au serveur BD...")
        serveur=ServerProxy(ad)
        return serveur
        
if __name__ == '__main__':
    c=Controleur()