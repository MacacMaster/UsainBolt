import sqlite3
    
class ServeurBDcas():
    def __init__(self,pControleur):
        self.etat="NonTerminé"
        self.database = sqlite3.connect('cas.db')
        self.curseur = self.database.cursor()
        self.curseur.execute("select * from client")
        self.id = len(self.curseur.fetchall())
        
        
    def modifierCas(self,cas,usager,machine,indice):
       
        self.curseur.execute("UPDATE client SET cas=? WHERE id=?", (cas,indice,))
        self.curseur.execute("UPDATE client SET usager=? WHERE id=?", (usager,indice,))
        self.curseur.execute("UPDATE client SET machine=? WHERE id=?", (machine,indice,))
        self.database.commit()
        
        
    def envoyerCas(self,cas,usager,machine):
        self.id+=1
        self.curseur.execute("INSERT INTO client VALUES (?,?,?,?,?);", (self.id,cas, usager, machine,self.etat))
        self.database.commit()
    
    def chercherBdcas(self,id):
        print("Id",id)
        cas=self.curseur.execute("SELECT cas FROM client WHERE id=?", (id,))
        print("cas",cas)
        return cas.fetchone()[0]
    
    def chercherBdUtilisateur(self,id):
        print("Id",id)
        usager=self.curseur.execute("SELECT usager FROM client WHERE id=?", (id,))
        return usager.fetchone()[0] 
    
    def chercherBdMachine(self,id):
        machine=self.curseur.execute("SELECT machine FROM client WHERE id=?", (id,))
        return machine.fetchone()[0] 
    
    def changerEtat(self,etatInitial):
        etat=self.curseur.execute('SELECT etat FROM client WHERE id=?',(etatInitial+1,))
        etatCompare=etat.fetchone()[0]
        if(etatCompare=="NonTerminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("Terminé",etatInitial+1,"NonTerminé",))
        elif(etatCompare=="Terminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("NonTerminé",etatInitial+1,"Terminé",))
        elif(etatCompare=="Reprendre"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("NonTerminé",etatInitial+1,"Reprendre",))
            self.database.commit()
            return False
        self.database.commit()
    
    def changerEtatReprendre(self,etatInitial):
        etat=self.curseur.execute('SELECT etat FROM client WHERE id=?',(etatInitial+1,))
        etatCompare=etat.fetchone()[0]
        if(etatCompare=="NonTerminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("Reprendre",etatInitial+1,"NonTerminé",))
        elif(etatCompare=="Terminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("Reprendre",etatInitial+1,"Terminé",))
        self.database.commit()
        
        
    def remplirListeUsager(self):
        listeUsager=[]
        for cas in self.curseur.execute('SELECT utilisateur FROM client'):
            listeUsager.append(cas)
            
    def remplirListeCas(self):
        listeCas=[]
        for cas in self.curseur.execute('SELECT cas FROM client'):
            listeCas.append(cas)
        return listeCas
        
    def remplirListeEtat(self):
        listeEtat=[]
        for etat in self.curseur.execute('SELECT etat FROM client'):
            listeEtat.append(etat)
        return listeEtat