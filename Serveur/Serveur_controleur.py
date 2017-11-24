#-*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
 #création de l'objet qui écoute  Q
import socket
import sqlite3
from xmlrpc.client import ServerProxy
from subprocess import Popen
import os

class Client(object):
    def __init__(self,nom):
        self.nom=nom
        self.cadreCourant=0
        self.cadreEnAttenteMax=0
        self.actionsEnAttentes={}
        
        
class ModeleService(object):
    def __init__(self,pControleur):
        self.controleur=pControleur
        #{Clé outils disponible:}
        self.modulesdisponibles={"projet":"projet","Mandat":"Mandat","CasUsage":"CasUsage"}# "CasUsage" : "CasUsage"}

        self.outilsdisponibles={"meta_sql": "meta_sql",}
        self.clients={}

    def creerclient(self,nom):
        if nom in self.clients.keys(): # on assure un nom unique
            return [0,"Simulation deja en cours"]
        # tout va bien on cree le client et lui retourne la seed pour le random
        c=Client(nom)
        self.clients[nom]=c
        return [1,"Bienvenue",list(self.modulesdisponibles.keys()),list(self.outilsdisponibles.keys())]


class ControleurServeur():
    def __init__(self):
        self.modele= ModeleService(self)
        self.serveurBD=None
        
    def logInServeur(self, pUsagerIP, pIdentifiantNomUsager, pIdentifiantNomOrga, pIdentifiantMotDePasse):
        #Connection au serveurDB
        ad="http://"+pUsagerIP+":9998"
        print("Connection au serveur BD...")
        self.serveurBD=ServerProxy(ad)
        print("Connection serveur BD réussi")
        
        #variables id
        identifiantNomUsager = pIdentifiantNomUsager
        identifiantNomOrga = pIdentifiantNomOrga
        identifiantMotDePasse = pIdentifiantMotDePasse
       # rep = self.serveurBD.selDonnees(Organisation, Nom)
        nomClientTempo = self.chercherClientBD(identifiantNomUsager, identifiantNomOrga, identifiantMotDePasse)
        if (nomClientTempo == 0):
            return 0
        else:
            print("Recherche du client terminé. Il s'agit de", nomClientTempo)
            client = self.modele.creerclient(nomClientTempo)
            return client

    def finDuProgramme(self):
        daemon.shutdown()
        
    def chercherClientBD(self, pIdentifiantNom, pIdenfiantOrga, pIdentifiantMotDePasse):
        nomClientTempo = self.serveurBD.chercherClientBD(pIdentifiantNom, pIdenfiantOrga, pIdentifiantMotDePasse)
        return nomClientTempo
    
    def requeteModule(self,mod):
        if mod in self.modele.modulesdisponibles.keys():
            cwd=os.getcwd()
            #print(mod,os.getcwd())
            if os.path.exists(cwd+"/modules/"):
                dirmod=cwd+"/modules/"+self.modele.modulesdisponibles[mod]+"/"
                if os.path.exists(dirmod):
                    #print("TROUVE")
                    listefichiers=[]
                    for i in os.listdir(dirmod):
                        if os.path.isfile(dirmod+i):
                            val=["fichier",i]
                        else:
                            val=["dossier",i]
                            
                        listefichiers.append(val)
                    return [mod,dirmod,listefichiers]
                
    def requeteOutil(self,mod):
        if mod in self.modele.outilsdisponibles.keys():
            cwd=os.getcwd()
            #print(mod,os.getcwd())
            if os.path.exists(cwd+"/outils/"):
                dirmod=cwd+"/outils/"+self.modele.outilsdisponibles[mod]+"/"
                if os.path.exists(dirmod):
                    #print("TROUVE")
                    listefichiers=[]
                    for i in os.listdir(dirmod):
                        if os.path.isfile(dirmod+i):
                            val=["fichier",i]
                        else:
                            val=["dossier",i]
                            
                        listefichiers.append(val)
                    return [mod,dirmod,listefichiers]
                
                
    def requeteFichier(self,lieu):
        fiche=open(lieu,"rb")
        contenu=fiche.read()
        fiche.close()
        return xmlrpc.client.Binary(contenu)
    
    #Fonction d'écriture du log        
    def writeLog(self,date,org,user,ip,db,module,action):
        logLocation='Logs.sqlite'
        logdb = sqlite3.connect(logLocation)
        curseur = logdb.cursor()
        curseur.execute("INSERT INTO logs VALUES(?,?,?,?,?,?,?)", (date,org,user,ip,db,module,action,))
        logdb.commit()
        logdb.close()
        return True 
    
print("Création du serveur...")
daemon = SimpleXMLRPCServer((socket.gethostbyname(socket.gethostname()),9999))
objetControleurServeur=ControleurServeur()
daemon.register_instance(objetControleurServeur)
print("Création du serveur terminé")
daemon.serve_forever()
