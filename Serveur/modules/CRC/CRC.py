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
        self.root.title("MANDAT")
        self.hauteurTotale=200
        self.largeurTotale=200
        self.hauteurMandat=200
        self.largeurMandat=200
        self.fenetre = Frame(master=self.root, width=self.largeurTotale, height=self.hauteurTotale, bg="steelblue")
        self.fenetre.pack()
    
    
    def creerVueMenu(self):
        self.menu = Frame(master=self.fenetre, width=500,height=800,bg="steelblue")
    
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