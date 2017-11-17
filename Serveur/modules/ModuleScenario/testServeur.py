#-*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
 #création de l'objet qui écoute  Q
import socket
import sqlite3

class Client(object):
    def __init__(self,nom, ip):
        self.nom = nom
        self.ip = ip
        
    def getNom(self):
        return self.nom;

class ModeleService():
    def __init__(self,pControleurServeur):
        self.controleurServeur = pControleurServeur
        self.etatJeu=0
        self.clients={}

    def creerClient(self, pClientNom, pClientIp):
        nom = pClientNom
        ip = pClientIp
        if self.etatJeu==0:  # si le jeu n'est pas partie sinon voir else
            if nom in self.clients.keys(): # on assure un nom unique
                return [0,"Erreur de nom"]
            c=Client(nom, ip)
            self.clients[nom]=c
            print(self.client[nom])
            return [1,"Bienvenue"]
        else:
            return [0,"Simulation deja en cours"]
    

class ControleurServeur():
    def __init__(self):
        self.database = sqlite3.connect('fightus.db')
        self.curseur = self.database.cursor()
        self.modele=ModeleService(self)
        
    def logInServeur(self, pIdentifiantNom, pIdentifiantMotDePasse):
        identifiantNom = pIdentifiantNom
        pIdentifiantMotDePasse = pIdentifiantMotDePasse
        clientTempo = self.chercherClientBD(identifiantNom, pIdentifiantMotDePasse)
        print("Recherche du client terminé. Il s'agit de", clientTempo)
        return clientTempo

    def finDuProgramme(self):
        daemon.shutdown()
        
    def chercherClientBD(self, pIdentifiantNom, pIdentifiantMotDePasse):
        nomClientExiste = False
        mdpClientExiste = False
        
        print("Authentification en cours...")
        for nomClient in self.curseur.execute('SELECT nomClient FROM client'):
            print(str(nomClient)[2:len(nomClient)-4])
            if (str(nomClient)[2:int(len(nomClient)-4)] == pIdentifiantNom):
                nomClientExiste = True
                break
        for mdpClient in self.curseur.execute('SELECT motDePasseClient FROM client'):
            print(str(mdpClient)[2:len(mdpClient)-4])
            if (str(mdpClient)[2:len(mdpClient)-4] == pIdentifiantMotDePasse):
                mdpClientExiste = True
                break
        if (nomClientExiste and mdpClientExiste):
            print("Réussite de l'authentification")
            return str(nomClient)[2:int(len(nomClient)-4)]
        else:
            print("Echec de l'authentification")
            return 0

print("Création du serveur...")
daemon = SimpleXMLRPCServer((socket.gethostbyname(socket.gethostname()),9999))
objetControleurServeur=ControleurServeur()
daemon.register_instance(objetControleurServeur)
print("Création du serveur terminé")
daemon.serve_forever()