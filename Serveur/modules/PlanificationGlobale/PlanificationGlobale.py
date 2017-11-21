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
        self.root.title("PLanification Globale")
        self.hauteurTotale=600
        self.largeurTotale=800
        self.hauteurMandat=200
        self.largeurMandat=600
        self.fenetre = Frame(master=self.root, width=self.largeurTotale, height=self.hauteurTotale, bg="steelblue")
        self.fenetre.pack()
        self.text = ""
        self.mot=""
                      

        self.barreTaches()

    def barreTaches(self):
        #menu deroulante

        self.menubar = Menu(self.root)
        self.menubar.add_command(label="Enregistrer", command= lambda: self.parent.modele.enregistrer(self.text))
        self.menubar.add_command(label="Charger un fichier", command= lambda: self.parent.modele.explorateurFichiers(self.text))
        self.menubar.add_separator()
        self.menubar.add_command(label=self.parent.modele.getTime(), command= lambda: self.parent.modele.enregistrer(self.text))
        self.root.config(menu=self.menubar)

    def fenetreConfirmation(self):
        pass
    
    
  
class Modele():
    def __init__(self, parent):
        pass
        
    def importerDonnees(self,projectName):
        pass

    def getTime(self):
        return (datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
class SQL():
    def __init__(self, adresseServeur):
        self.adresseServeur=adresseServeur
        
        pass
            


class Controleur():
    def __init__(self):
        #Adresse du ServeurDB
        self.dbip="127.0.0.1"
        self.adresseServeur="http://"+self.dbip+":9998"
        self.organisation=""
        self.user=""
        self.clientip=""
        self.modele=Modele(self)
        #self.serveur = self.connectionServeur()
        self.vue=Vue(self)
        self.vue.root.mainloop()
    
    def fermerProgramme(self):
        
        exit
        
    def writeLog(self,action="Actionman",module="Client"):
        #print(self.getTime() + " "+self.organisation + " "+self.user + " "+self.clientip + " "+self.dbip + " "+module + " "+action)
        self.parent.serveur.writeLog(self.modele.getTime(),self.organisation,self.user,self.clientip,self.dbip,module,action)

        
    
    def connectionServeurDB(self):
        print("Connection au serveur BD...")
        serveur=ServerProxy(self.adresseServeur)
        return serveur
        
if __name__ == '__main__':
    #parent = serveur Saas
    c=Controleur()