#-*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
 #création de l'objet qui écoute  Q
import socket
import sqlite3

class ControleurServeurBD():
    def __init__(self):
        self.database = sqlite3.connect('SprintMasterData.db')
        self.curseur = self.database.cursor()
        
    def chercherClientBD(self, pIdentifiantNom, pIdentifiantOrga, pIdentifiantMotDePasse):
        nomOrgaExiste = False
        nomUsaExiste = False
        mdpExiste = False
            
        print("Authentification en cours...")
        
        for nomOrga in self.curseur.execute('SELECT nomOrganisation FROM organisation'):
            print(str(nomOrga)[2:len(nomOrga)-4])
            if (str(nomOrga)[2:int(len(nomOrga)-4)] == pIdentifiantOrga):
                nomOrgaExiste = True
                break
            
        for nomUsager in self.curseur.execute('SELECT nomUsager FROM organisation'):
            print(str(nomUsager)[2:len(nomUsager)-4])
            if (str(nomUsager)[2:int(len(nomUsager)-4)] == pIdentifiantNom):
                nomUsaExiste = True
                break
        
        for mdp in self.curseur.execute('SELECT motDePasse FROM organisation'):
            print(str(mdp)[2:len(mdp)-4])
            if (str(mdp)[2:len(mdp)-4] == pIdentifiantMotDePasse):
                mdpExiste = True
                break
            
        if (nomOrgaExiste and nomUsaExiste and mdpExiste):
            print("Réussite de l'authentification")
            return pIdentifiantNom
        else:
            print("Echec de l'authentification")
            return 0

print("Création du serveur pour la BD...")
daemon = SimpleXMLRPCServer((socket.gethostbyname(socket.gethostname()),9998))
objetControleurServeurBD=ControleurServeurBD()
daemon.register_instance(objetControleurServeurBD)
print("Création du serveur BD terminé")
daemon.serve_forever()