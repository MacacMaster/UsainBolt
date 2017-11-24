#-*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
 #création de l'objet qui écoute  Q
import socket
import sqlite3

class ControleurServeurBD():
    def __init__(self):
        self.database = sqlite3.connect('BDD.sqlite')
        self.curseur = self.database.cursor()
        
    def insDonnees(self,nomTable,valeurs):
        conn= sqlite3.connect('BDD.sqlite')
        c = conn.cursor()
        c.execute(s)
        conn.commit()
        conn.close()
    
    def selDonnees(self,nomTable,idCol):
        conn= sqlite3.connect('BDD.sqlite')
        c = conn.cursor()
        c.execute(''' SELECT * from Projets''') 
        #c.execute('''SELECT ''' +idCol+ ''' from '''+nomTable)
        print(c.fetchall())
        conn.close()
        
    def chercherClientBD(self, pIdentifiantNom, pIdentifiantOrga, pIdentifiantMotDePasse):
        nomOrgaExiste = False
        nomUsaExiste = False
        mdpExiste = False
            
        print("Authentification en cours...")
        
        for nomOrga in self.curseur.execute('SELECT Nom FROM organisation'):
            print(str(nomOrga)[2:len(nomOrga)-4])
            if (str(nomOrga)[2:int(len(nomOrga)-4)] == pIdentifiantOrga):
                nomOrgaExiste = True
                break
            
        for nomUsager in self.curseur.execute('SELECT nom FROM usagers'):
            print(str(nomUsager)[2:len(nomUsager)-4])
            if (str(nomUsager)[2:int(len(nomUsager)-4)] == pIdentifiantNom):
                nomUsaExiste = True
                break
        
        for mdp in self.curseur.execute('SELECT Motdepasse FROM usagers'):
            print(str(mdp)[2:len(mdp)-4])
            if (str(mdp)[2:len(mdp)-4] == pIdentifiantMotDePasse):
                mdpExiste = True
                break
            
        if (nomOrgaExiste and nomUsaExiste and mdpExiste):
            print("Réussite de l'authentification")
            nomOrga = (''+pIdentifiantNom+'',)
            idOrgaBD = self.curseur.execute("SELECT id FROM Usagers WHERE Organisation_Id = ?", nomOrga)
            idOrga = idOrgaBD.fetchone()
            print("id de la personne connectée:", str(idOrga)[1:len(idOrga)-3])
            return [pIdentifiantNom, str(idOrga)[1:len(idOrga)-3]]
        else:
            print("Echec de l'authentification")
            return 0
        

         

    def rechercheProjetsDispo(self, id):
        print("je cherche des projets")
        t = (''+str(id)+'',)
        tabProjet = []
        for projet in self.curseur.execute('SELECT nom FROM Projets WHERE Organisation_Id =?', t):
            print (str(projet)[2:len(projet)-4])
            tabProjet.append(str(projet)[2:len(projet)-4])
        return tabProjet

    
    
print("Création du serveur pour la BD...")
daemon = SimpleXMLRPCServer((socket.gethostbyname(socket.gethostname()),9998),allow_none = 1)
objetControleurServeurBD=ControleurServeurBD()
daemon.register_instance(objetControleurServeurBD)
print("Création du serveur BD terminé")
daemon.serve_forever()



