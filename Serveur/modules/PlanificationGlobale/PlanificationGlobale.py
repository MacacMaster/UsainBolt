#-*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import *
import sqlite3
from datetime import datetime
from _overlapped import NULL

from PlanificationGlobaleVue  import *

    
    
  
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
        sys.argv[0] #nom du .py
        #sys.argv[1]
        #Adresse du ServeurDB
        #self.dbip="127.0.0.1"
        #self.adresseServeur="http://"+self.dbip+":9998"
        self.saasip=""
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