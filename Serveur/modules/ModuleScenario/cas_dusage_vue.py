from tkinter import *
from logging.config import listen
import sqlite3

class Controleur():
    def __init__(self):
        
        self.etat="NonTerminé"
        
        self.database = sqlite3.connect('cas.db')
        self.curseur = self.database.cursor()
        self.curseur.execute("select * from client")
        self.id = len(self.curseur.fetchall())
        self.vue = Vue(self)
        self.modele= Modele(self)
        self.vue.root.mainloop()
        
    def modifierCas(self,cas,usager,machine):
        self.curseur.execute("UPDATE client SET cas=? WHERE id=?", (cas,self.vue.indiceCasModifier+1,))
        self.curseur.execute("UPDATE client SET usager=? WHERE id=?", (usager,self.vue.indiceCasModifier+1,))
        self.curseur.execute("UPDATE client SET machine=? WHERE id=?", (machine,self.vue.indiceCasModifier+1,))
        self.database.commit()
        
        
    def envoyerCas(self,cas,usager,machine):
        self.id+=1
        self.curseur.execute("INSERT INTO client VALUES (?,?,?,?,?);", (self.id,cas, usager, machine,self.etat))
        self.vue.mettreAJourListes()
        self.database.commit()
    
    def chercherBd(self):
        self.vue.recevoirDonnees(liste)
        
    def changerReprendre(self):
        etat=self.curseur.execute('SELECT etat FROM client WHERE id=?',(self.vue.indiceCasModifier+1,))
        etatCompare=etat.fetchone()[0]
        if(etatCompare=="NonTerminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("Reprendre",self.vue.indiceCasModifier+1,"NonTerminé",))
        elif(etatCompare=="Terminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("Reprendre",self.vue.indiceCasModifier+1,"Terminé",))
        self.vue.caneva.forget()
        self.database.commit()
        self.vue.menuInitial()
    
    def changerTermineNonTermine(self):
        etat=self.curseur.execute('SELECT etat FROM client WHERE id=?',(self.vue.indiceCasModifier+1,))
        etatCompare=etat.fetchone()[0]
        if(etatCompare=="NonTerminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("Terminé",self.vue.indiceCasModifier+1,"NonTerminé",))
        elif(etatCompare=="Terminé"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("NonTerminé",self.vue.indiceCasModifier+1,"Terminé",))
        elif(etatCompare=="Reprendre"):
            self.curseur.execute("UPDATE client SET etat=? WHERE id=? AND etat=?", ("NonTerminé",self.vue.indiceCasModifier+1,"Reprendre",))
            self.vue.unReprend=False
        self.vue.caneva.forget()
        self.database.commit()
        self.vue.menuInitial()
        
class Modele():
    def __init__(self, pControleur):
        self.controleur = pControleur
    
class Vue():
    def __init__(self, pControleur):
        self.controleur = pControleur
        self.largeur = 800
        self.hauteur = 600
        self.root = Tk()
        self.fenetre = Frame(self.root, width = self.largeur, height = self.hauteur)
        self.fenetre.pack()
        self.liste={"a","b","c","a2","b2","c2"}
        self.listeCas=[]
        self.listeEtat=[]
        self.dejaOuvert=False
        self.unReprend=False
        self.menuInitial()
        self.indiceCasModifier=0
        
    

    def mettreAJourListes(self):
        self.remplirListeEtat()
        self.remplirListeCas()
        self.remplirListBoxEtat()
        self.remplirListBoxCas()    
    
    def remplirListeCas(self):
        for cas in self.controleur.curseur.execute('SELECT cas FROM client'):
            self.listeCas.append(cas)
        
    def remplirListeEtat(self):
        for etat in self.controleur.curseur.execute('SELECT etat FROM client'):
            self.listeEtat.append(etat)
        
    def menuInitial(self):
        
        self.caneva = Canvas(self.fenetre, width = self.largeur, height=self.hauteur, bg="steelblue")
        self.caneva.pack()
        self.labnbe=Label(text="Cas d'usage       ",bg="lightblue")
        self.caneva.create_window(150,50,window=self.labnbe)
        self.labelCasUsage=Entry(bg="white")
        self.caneva.create_window(150,120,window=self.labelCasUsage,width=150,height=100)
        
        self.labnbe=Label(text="Action usager    ",bg="lightblue")
        self.caneva.create_window(400,50,window=self.labnbe)
        self.labelActionUsager=Entry(bg="white")
        self.caneva.create_window(400,120,window=self.labelActionUsager,width=150,height=100)
        self.labnbe=Label(text="Action machine",bg="lightblue")
        self.caneva.create_window(650,50,window=self.labnbe)
        self.labelActionMachine=Entry(bg="white")
        self.caneva.create_window(650,120,window=self.labelActionMachine,width=150,height=100)

        self.btnEnvoyerUsager=Button(self.caneva,text="Envoyer",width=20,command=self.envoyerTexte)
        self.caneva.create_window(400,200,window=self.btnEnvoyerUsager,width=150,height=20)
    
        self.btnModifier=Button(self.caneva,text="Modifier",width=20,command=self.indiceDeLaBD)
        self.caneva.create_window(700,550,window=self.btnModifier,width=150,height=20)
        
        self.bntSupprimer=Button(self.caneva,text="Terminé/NonTerminé",width=20,command=self.termineNonTermine)
        self.caneva.create_window(100,550,window=self.bntSupprimer,width=150,height=20)
        
        self.bntReprendre=Button(self.caneva,text="Reprendre",width=20,command=self.reprendre)
        self.caneva.create_window(self.largeur/2,550,window=self.bntReprendre,width=150,height=20)
        
        self.listeetat=Listbox(self.caneva,bg="lightblue",borderwidth=0,relief=FLAT,width=12,height=12)
        self.caneva.create_window(670,350,window=self.listeetat)

        self.listecas=Listbox(self.caneva,bg="lightblue",borderwidth=0,relief=FLAT,width=90,height=12)
        self.caneva.create_window(350,350,window=self.listecas)
        self.remplirListeEtat()
        self.remplirListeCas()
        self.remplirListBoxEtat()
        self.remplirListBoxCas()
        
        if(self.dejaOuvert==False):
            self.ouvrirReprendre()
        
    def unSeulReprendre(self):
        for i in range(1,self.listeetat.size()+1):
            etat=self.listeetat.get(ACTIVE)
            self.listeetat.activate(i)
            etat2= str(etat)
            if(etat2=="('Reprendre',)"):
                self.unReprend=True
                
                
    def ouvrirReprendre(self):
        compteur=0
        for i in range(1,self.listeetat.size()+1):
            compteur+=1
            etat=self.listeetat.get(ACTIVE)
            self.listeetat.activate(i)
            etat2= str(etat)
            if(etat2=="('Reprendre',)"):
                self.indiceCasModifier=compteur-1
                self.dejaOuvert=True
                self.menuModifier()  
               
        
    def reprendre(self):
        self.unSeulReprendre()
        if(self.unReprend==False):  
            self.indiceCasModifier=self.listeetat.curselection()[0]
            self.controleur.changerReprendre()
    
        
    def indiceDeLaBD(self):
        self.indiceCasModifier=self.listecas.curselection()[0]
        self.menuModifier()
        
    def recevoirDonnees(self,liste):
        pass
    
    def remplirListBoxCas(self):
        self.listecas.delete(0, END)
        for i in self.listeCas:
            self.listecas.insert(END,i)
        self.listeCas.clear()
            
    def remplirListBoxEtat(self):
        self.listeetat.delete(0, END)
        for i in self.listeEtat:
            self.listeetat.insert(END,i)
        self.listeEtat.clear()
        
    def menuModifier(self):
        self.caneva.forget()
        self.canevaMod = Canvas(self.fenetre, width = self.largeur, height=self.hauteur, bg="steelblue")
        self.canevaMod.pack()
        self.labnbe=Label(text="Cas d'usage       ",bg="lightblue")
        self.canevaMod.create_window(150,50,window=self.labnbe)
        self.labelCasUsage=Entry(bg="white")
        self.canevaMod.create_window(150,200,window=self.labelCasUsage,width=150,height=250)
        
        self.labnbe=Label(text="Action usager    ",bg="lightblue")
        self.canevaMod.create_window(400,50,window=self.labnbe)
        self.labelActionUsager=Entry(bg="white")
        self.labelActionMachine=Entry(bg="white")
        self.canevaMod.create_window(650,200,window=self.labelActionMachine,width=150,height=250)
        cas=self.controleur.curseur.execute("SELECT cas FROM client WHERE id=?", (self.indiceCasModifier+1,))
        self.labelCasUsage.insert(END, cas.fetchone()[0])
        usager=self.controleur.curseur.execute("SELECT usager FROM client WHERE id=?", (self.indiceCasModifier+1,))
        self.labelActionUsager.insert(END, usager.fetchone()[0] )
        machine=self.controleur.curseur.execute("SELECT machine FROM client WHERE id=?", (self.indiceCasModifier+1,))
        self.labelActionMachine.insert(END,machine.fetchone()[0] )
        self.canevaMod.create_window(400,200,window=self.labelActionUsager,width=150,height=250)
        self.labnbe=Label(text="Action machine",bg="lightblue")
        self.canevaMod.create_window(650,50,window=self.labnbe)
        

        self.btnEnvoyerUsager=Button(self.canevaMod,text="Envoyer",width=20,command=self.envoyerTexte)
        self.canevaMod.create_window(400,200,window=self.btnEnvoyerUsager,width=150,height=20)
    
        self.btnRetour=Button(self.canevaMod,text="Retour",width=20,command=self.menuInitialMod)
        self.canevaMod.create_window(100,550,window=self.btnRetour,width=150,height=20)
        
        
        self.bntModifier=Button(self.canevaMod,text="Modifier",width=20,command=self.modifierTexte)
        self.canevaMod.create_window(150,400,window=self.bntModifier,width=150,height=20)
        
        
        self.bntAction=Button(self.canevaMod,text="Prochaine action",width=20,command=self.changerAction)
        self.canevaMod.create_window(600,400,window=self.bntAction,width=150,height=20)
        
       
        
       
        
    def changerAction(self):
        pass 
    def termineNonTermine(self):
        self.indiceCasModifier=self.listeetat.curselection()[0]
        self.controleur.changerTermineNonTermine()
    def menuInitialMod(self):
        self.canevaMod.forget()
        self.menuInitial()
        
    def modifierTexte(self):
        cas=self.labelCasUsage.get()
        usager=self.labelActionUsager.get()
        machine=self.labelActionMachine.get()
        self.controleur.modifierCas(cas,usager,machine)
        self.labelActionUsager.delete(0, 'end')
        self.labelCasUsage.delete(0, 'end')
        self.labelActionMachine.delete(0, 'end')
    
    def envoyerTexte(self):
        cas=self.labelCasUsage.get()
        usager=self.labelActionUsager.get()
        machine=self.labelActionMachine.get()
        self.insererCas(cas,usager,machine)
        self.labelActionUsager.delete(0, 'end')
        self.labelCasUsage.delete(0, 'end')
        self.labelActionMachine.delete(0, 'end')
        
    
    
    def insererCas(self,cas,usager,machine):
       self.controleur.envoyerCas(cas,usager,machine)
    
if __name__ == '__main__':
    c = Controleur()