# -*- coding: utf-8 -*-

#import Pyro4
import socket
from tkinter import *
from tkinter import messagebox
from  xmlrpc.client import ServerProxy
from subprocess import Popen 

class Vue():
    def __init__(self,pControleur,pClientIp):
        self.controleur = pControleur
        self.largeur = 800
        self.hauteur = 600
        self.cadreActuel = None
        self.root=Tk()
        self.root.title("testJeu")
        self.root.protocol("WM_DELETE_WINDOW", self.controleur.fermerApplication)
        self.cadreApplication = Frame(self.root, width = self.largeur, height = self.hauteur)
        self.cadreApplication.pack()
        self.centrerFenetre()
        
        self.creerCadreLogIn(pClientIp)
        self.cadreCompteClient()
        self.cadreLobby()
        
        self.changeCadre(self.cadreLogIn)
    
    def centrerFenetre(self):
        self.root.update() # Suivant le WM. A faire dans tous les cas donc.
        fenrw = self.root.winfo_reqwidth()
        fenrh = self.root.winfo_reqheight()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+%d+%d" % (fenrw, fenrh, (sw-fenrw)/2, (sh-fenrh)/2))
    
    def changeCadre(self,cadre):
        if self.cadreActuel:
            self.cadreActuel.pack_forget()
        self.cadreActuel=cadre
        self.cadreActuel.pack()
            
    def creerCadreLogIn(self,ip):
        largeur = self.root.winfo_reqwidth()
        hauteur = self.root.winfo_reqheight()
        self.cadreLogIn=Frame(self.cadreApplication)
        self.canevaLogIn=Canvas(self.cadreLogIn,width=largeur,height=hauteur)
        self.image = PhotoImage(file="bg_connection.gif")
        largeurImage, hauteurImage = self.image.width(), self.image.height()
        self.canevaLogIn.create_image((largeurImage//2, hauteurImage//2), image=self.image)
        self.entrerNom=Entry(bg="white")
        self.entrerMotDePasse=Entry(bg="white", show="*")
        btnLogInClient=Button(text="Jouer", command=self.logInClient, relief = FLAT)
        self.canevaLogIn.create_window(largeur/2,hauteur-hauteur/3.8,window=self.entrerNom,width=150,height=30)
        self.canevaLogIn.create_window(largeur/2,hauteur-hauteur/5,window=self.entrerMotDePasse,width=150,height=30)
        self.canevaLogIn.create_window(largeur/2,hauteur-hauteur/8,window=btnLogInClient,width=150,height=30) 
        self.canevaLogIn.pack()
        
    def cadreCompteClient(self):
        largeur = self.root.winfo_reqwidth()
        hauteur = self.root.winfo_reqheight()
        self.cadreCompteClient = Frame(self.cadreApplication)
        self.canevaCompteClient = Canvas(self.cadreCompteClient,width=largeur,height=hauteur, bg = "black")
        btnCreerLobby=Button(text="Créer une partie", command=self.creerLobby, relief = FLAT)
        btnCherchePartie=Button(text="Rejoindre une partie", command=self.cherchePartie, relief = FLAT)
        self.canevaCompteClient.create_window(largeur-150,hauteur-hauteur/5,window=btnCreerLobby,width=150,height=30) 
        self.canevaCompteClient.create_window(largeur-150,hauteur-hauteur/8,window=btnCherchePartie,width=150,height=30) 
        self.canevaCompteClient.pack()
        
    def logInClient(self):
        identifiantNom = self.entrerNom.get()
        identifiantMotDePasse = self.entrerMotDePasse.get()
        print("Nom entré par l'usager ", identifiantNom, "Mot de passe entré par l'usager ", identifiantMotDePasse)
        self.controleur.logInClient(identifiantNom, identifiantMotDePasse)
    
    def logInClientFail(self):
        messagebox.showwarning('Connexion refusée', 'Nom de compte ou mot de passe incorrecte')
        
    def logInClientSuccess(self):
        self.changeCadre(self.cadreCompteClient)
        
    def creerLobby(self):
        self.controleur.creerLobby()
        self.changeCadre(self.cadreLobby)
        
    def cadreLobby(self):    
        largeur = self.root.winfo_reqwidth()
        hauteur = self.root.winfo_reqheight()
        self.cadreLobby = Frame(self.cadreApplication)
        self.canevaLobby = Canvas(self.cadreLobby,width=largeur,height=hauteur, bg = "black")
        labNom=Label(text="Orion mini",bg="sky blue",borderwidth=0,relief=RIDGE,fg="black", font=("Helvetica", 28))
        btnPret=Button(text="Pret", relief = FLAT)
        self.canevaLobby.create_window(largeur-150,hauteur-hauteur/8,window=btnPret,width=150,height=30)
        self.canevaLobby.pack()
    
    def cherchePartie(self):
        pass

class Controleur():
    def __init__(self):
        self.clientIP = self.chercherIP()
        self.serveur=None
        self.vue=Vue(self,self.clientIP)
        self.vue.root.mainloop()
        
    def chercherIP(self):
        clientIP = socket.gethostbyname(socket.gethostname())
        print("L'addresse ip du client est: ", clientIP)
        return clientIP

    def fermerApplication(self):
        self.vue.root.destroy()
        
    def logInClient(self, pIdentifiantNom, pIdentifiantMotDePasse):
        ad="http://"+self.clientIP+":9999"
        print("Création du serveur en cours...")
        self.serveur=ServerProxy(ad)
        print("Création du serveur réussi")
        reponseServeur = self.serveur.logInServeur(pIdentifiantNom, pIdentifiantMotDePasse)
        if (reponseServeur == 0):
            self.vue.logInClientFail()
        else:
            self.vue.logInClientSuccess()

    def creerLobby(self):
        if self.egoserveur==0:
            pid = Popen(["C:\\Python34\\Python.exe", "./testServeur.py"],shell=1).pid
            self.egoserveur=1

if __name__=="__main__":
    c=Controleur()