#-*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import *
import sqlite3
from datetime import datetime
from _overlapped import NULL



class Vue():
    def __init__(self, parent):
        self.parent=parent
        self.root=Tk() #Fenetre
        self.root.title("Planification Globale")
        self.hauteurTotale=600
        self.largeurTotale=800
        self.hauteurSub=500
        self.largeurSub=800
        self.fenetre = Frame(master=self.root, width=self.largeurTotale, height=self.hauteurTotale, bg="steelblue")
        self.fenetre.pack()
                   

        self.barreTaches()
        #self.fenetreCreation()
        
    def barreTaches(self):
        #menu deroulante

        self.menubar = Menu(self.root)
        self.menubar.add_command(label="Enregistrer", command= NULL)
        self.menubar.add_command(label="Charger un fichier", command= print("HYPE!"))
        self.menubar.add_separator()
        #self.menubar.add_command(label=self.parent.modele.getTime())#, command= lambda: self.parent.modele.enregistrer(self.text))
        self.root.config(menu=self.menubar)

    def fenetreCreation(self):
        self.fentrecreationplanif = Frame(self.fenetre,width=self.largeurSub, height=self.hauteurSub)
        self.btnSauvegarder=Button(self.fentrecreationplanif)
        
        self.lbltemps=Label(self.fentrecreationplanif,font=("Arial",15,"bold"), bg="white")
        self.lbltemps.configure(text=" " + str(self.parent.modele.getTime))
        self.lblcrc= Label(master=self.fentrecreationplanif,text="")
        self.fentrecreationplanif.pack()
        pass
    
    
    def fenetreConfirmation(self):
        
        pass