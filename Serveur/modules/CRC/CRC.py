#-*- coding: utf-8 -*-

from xmlrpc.client import ServerProxy
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
from tkinter import messagebox
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
        self.collaborateurs=[]
        self.responsabilites = []
        self.focused_box = None
        
    
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
        listeClasses = Listbox(frame2, height=25)
        listeClasses.pack(side=LEFT,fill="y")
        
        scrollbar = Scrollbar(frame2, orient = "vertical")
        scrollbar.config(command=listeClasses.yview)  
        scrollbar.pack(side=LEFT,fill="y")
   
        listeClasses.config(yscrollcommand=scrollbar.set)
          
        #for x in range(30):
        #    listeClasses.insert(END, str(x))

        
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
        
        #zone nom de la classe
        frame1 = Frame(self.menuAjout)
        frame1.pack(fill=X, pady=5)
        
        lblNomClasse = Label(frame1, text="Nom (classe)", width=25)
        lblNomClasse.pack(side=LEFT)  
        
        self.entryNomClasse = Entry(frame1, text="", width=25)
        self.entryNomClasse.pack(side=LEFT)
        #entryNomClasse.insert(END,"nom de la classe");
        
        #zone propriétaire
        frame2 = Frame(self.menuAjout)
        frame2.pack(fill=X, pady=5)
        
        lblProprietaire = Label(frame2, text="Propriétaire", width=25)
        lblProprietaire.pack(side=LEFT)  
        
        self.entryProprietaire = Entry(frame2, width=25)
        self.entryProprietaire.pack(side=LEFT)
        #entryNomClasse.insert(END,"nom de la classe");
        
        #zone responsabilités et zone collaboration (labels)
        frame3 = Frame(self.menuAjout)
        frame3.pack(fill=X, pady=5)
        
        lblResponsabilite = Label(frame3, text="Responsabilité", width=25)
        lblResponsabilite.pack(side=LEFT)  
        
        lblCollaboration = Label(frame3, text="Collaboration", width=25)
        lblCollaboration.pack(side=LEFT)  
        
        #zone responsabilités et zone collaboration (champs)
        frame4 = Frame(self.menuAjout)
        frame4.pack(fill=X, pady=5)
        
        largeur = 55;
        self.entryResponsabilite = Entry(frame4, text="", width=15)
        self.entryResponsabilite.pack(side=LEFT, padx = largeur)
        self.entryResponsabilite.bind('<Return>',self.saisirResponsabilite)
        
        self.entryCollaboration = Entry(frame4, text="", width=15)
        self.entryCollaboration.pack(side=LEFT, padx = largeur)
        self.entryCollaboration.bind('<Return>',self.saisirCollaboration)
        
          
        #zone pour les listebox des responsabilités et des collaborations
        frameDeuxBox = Frame(self.menuAjout)
        frameDeuxBox.pack()
        
        #scrollbar gauche
        frame6 = Frame(frameDeuxBox)
        frame6.pack(fill=X, pady=5, side=LEFT)
        
        scrollbar = Scrollbar(frame6, orient = "vertical")
        
        self.listeResponsabilites = Listbox(frame6, height=25,yscrollcommand=scrollbar)
        self.listeResponsabilites.pack(side=LEFT, fill=BOTH, expand=1)
        self.listeResponsabilites.bind("<FocusIn>", self.box_focused)
        self.listeResponsabilites.bind("<FocusOut>", self.box_unfocused)
        
        scrollbar.config(command=self.listeResponsabilites.yview)  
        scrollbar.pack(side=LEFT,fill="y", expand=1)
        
        #scrollbar droite
        frame5 = Frame(frameDeuxBox)
        frame5.pack(fill=X, pady=5, side=LEFT)
        
        scrollbar = Scrollbar(frame5, orient = "vertical")
        
        self.listeCollaboration = Listbox(frame5, height=25,yscrollcommand=scrollbar)
        self.listeCollaboration.pack(side=LEFT, fill=BOTH, expand=1)
        self.listeCollaboration.bind("<FocusIn>", self.box_focused)
        self.listeCollaboration.bind("<FocusOut>", self.box_unfocused)
        
        scrollbar.config(command=self.listeCollaboration.yview)  
        scrollbar.pack(side=LEFT,fill="y", expand=1)
               
        #bouton en bas
        frame7 = Frame(self.menuAjout)
        frame7.pack(fill=X, pady=5)
        
        boutonConfirmer = Button(frame7, text="Confirmer", command = self.confirmer)
        boutonConfirmer.pack(side = LEFT)
        
        boutonSupprimer = Button(frame7, text="Supprimer", command = self.supprimer)
        boutonSupprimer.pack(side = LEFT)   
        
        boutonCanceler = Button(frame7, text="Canceler", command = self.canceler)
        boutonCanceler.pack(side = LEFT)         
        
    def canceler(self):
        #vider les listes, car aucune sauvegarde n'a été faite!
        self.listeCollaboration = []
        self.listeResponsabilites = []
        self.collaborateurs = []
        self.responsabilites = []  
        self.entryNomClasse.delete(0, END)
        self.entryNomClasse.insert(0, "")
        self.entryProprietaire.delete(0, END)
        self.entryProprietaire.insert(0, "")
        
        #enlever le menu qui existait
        self.menuAjout.pack_forget()
        
        #retour en arriere<
        self.menuGauche.pack(side=LEFT) 
        self.menuDroite.pack(side=LEFT) 
       
        
    def saisirCollaboration(self,event):
        saisie = self.entryCollaboration.get()
        self.collaborateurs.append(saisie)
        self.listeCollaboration.insert(END,saisie)
        #vider le Entry après avoir saisi quelque chose
        self.entryCollaboration.delete(0,END)
        print(self.entryCollaboration.get())
        
    def supprimer(self):
        if self.focused_box == self.listeCollaboration:
            index = self.listeCollaboration.curselection()[0]
            self.listeCollaboration.delete(index)
        elif self.focused_box == self.listeResponsabilites:
            index = self.listeResponsabilites.curselection()[0]
            self.listeResponsabilites.delete(index)
            
    def saisirResponsabilite(self,event):
        saisie = self.entryResponsabilite.get()
        self.responsabilites.append(saisie)
        self.listeResponsabilites.insert(END,saisie)
        #vider le Entry après avoir saisi quelque chose
        self.entryResponsabilite.delete(0,END)
        print(self.entryResponsabilite.get())
    
    def box_focused(self, event):
        self.focused_box = event.widget
        
    def box_unfocused(self, event):
        self.focused_box = None
        
    def confirmer(self):
        saisieNomClasse = self.entryNomClasse.get()
        saisieProprietaire = self.entryProprietaire.get()
        
        #mettre en jaune les infos manquantes
        if saisieNomClasse == "":
            self.entryNomClasse.configure({"background": "Yellow"})
        else:
            self.entryNomClasse.configure({"background": "White"})
        if saisieProprietaire == "":
            self.entryProprietaire.configure({"background": "Yellow"})
        else:
            self.entryProprietaire.configure({"background": "White"})        
        
        #affichage d'un message d'erreur
        if (saisieNomClasse == "" or saisieProprietaire == ""):
            print(saisieNomClasse)
            print(saisieProprietaire)

            messagebox.showwarning("Attention", "Saisir les informations manquantes")
        
        else: 
            self.canceler() #retour à au menu de base CRC  
            

class Modele():
    def __init__(self, parent, serveur):
        self.parent=parent
        self.serveur = serveur

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
    
    def nomsDesClasses(self):
        reponse = self.serveur.sel("CRCClasse", "nom")
        
        
        
        list = self.serveur.sel()
        return list
        

class Controleur():
    def __init__(self):
        #informations du système quand le programme est lancé
        #self.idClient = 999;
        self.ip = 999;
        self.idProjet = 999;
          
        #connexion au proxy
        ad="http://"+str(self.ip)+":9999"
        self.serveur = ServerProxy(ad)
        
        #self.serveur = self.connectionServeur()
        self.vue=Vue(self)
        self.vue.root.mainloop()
        self.modele=Modele(self, self.serveur)
    
    def connectionServeur(self):
        ad="http://"+pUsagerIP+":9998"
        print("Connection au serveur BD...")
        serveur=ServerProxy(ad)
        return serveur
        
if __name__ == '__main__':
    c=Controleur()