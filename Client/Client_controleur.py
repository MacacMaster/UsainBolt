# -*- coding: utf-8 -*-

from Client_modele  import *
from Client_vue import *
import socket
from xmlrpc.client import ServerProxy
from subprocess import Popen
import os

class Controleur():
    def __init__(self):
        
        #Debug: Ouvre automatiquement le Serveur Controleur  
        #pid1 = Popen(["C:\\Python34\\Python.exe", "../Serveur/Serveur_controleur.py"],shell=1).pid
        #Debug : Serveur BD refuses connection
        self.clientIP = self.chercherIP()
        self.serveur=None
        #self.log = Log(self,self.clientIP)
        self.vue=Vue(self,self.clientIP)
        self.vue.root.mainloop()
    
    #trouve l'IP du client
    def chercherIP(self):
        clientIP = socket.gethostbyname(socket.gethostname())
        print("L'addresse ip du client est: ", clientIP)
        return clientIP

    def fermerApplication(self):
        self.vue.root.destroy()
        
    def logInClient(self, pIdentifiantNomUsager, pIdentifiantNomOrga, pIdentifiantMotDePasse):
        #connection au Serveur
        ad="http://"+self.clientIP+":9999"
        print("Connection au serveur Saas en cours...")
        self.serveur=ServerProxy(ad)
        print("Connection au serveur Saas réussi")
        reponseServeur = self.serveur.logInServeur(self.clientIP, pIdentifiantNomUsager, pIdentifiantNomOrga, pIdentifiantMotDePasse)
        if (reponseServeur == 0):
            self.vue.logInClientFail()
        else:
            self.vue.chargerCentral(reponseServeur[2],reponseServeur[3])
            
    def requeteModule(self,mod):
        rep=self.serveur.requeteModule(mod)
        if rep:
            print(rep[0])
            cwd=os.getcwd()
            lieuApp="/"+rep[0]
            lieu=cwd+lieuApp
            print(lieu)
            if not os.path.exists(lieu):
                os.mkdir(lieu) #plante s'il exist deja
            reso=rep[1]
            print(rep[1])
            for i in rep[2]:
                if i[0]=="fichier":
                    nom=reso+i[1]
                    print("DODODOO",nom)
                    rep=self.serveur.requeteFichier(nom)
                    fiche=open(lieu+"/"+i[1],"wb")
                    fiche.write(rep.data)
                    fiche.close()
            chaineappli="."+lieuApp+lieuApp+".py"
            pid = Popen(["C:\\Python34\\Python.exe", chaineappli],shell=1).pid 
        else:
            print("RIEN")
            
               
    def requeteOutil(self,mod):
        rep=self.serveur.requeteOutil(mod)
        if rep:
            print(rep[0])
            cwd=os.getcwd()
            lieuApp="/"+rep[0]
            lieu=cwd+lieuApp
            print(lieu)
            if not os.path.exists(lieu):
                os.mkdir(lieu) #plante s'il exist deja
            reso=rep[1]
            print(rep[1])
            for i in rep[2]:
                if i[0]=="fichier":
                    nom=reso+i[1]
                    print("DODODOO",nom)
                    rep=self.serveur.requeteFichier(nom)
                    fiche=open(lieu+"/"+i[1],"wb")
                    fiche.write(rep.data)
                    fiche.close()
            chaineappli="."+lieuApp+lieuApp+".py"
            pid = Popen(["C:\\Python34\\Python.exe", chaineappli],shell=1).pid 
        else:
            print("RIEN")
            
if __name__=="__main__":
    c=Controleur()