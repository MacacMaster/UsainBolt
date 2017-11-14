# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from numpy.core.defchararray import center


class Vue():
    def __init__(self,parent,monip,largeur=800,hauteur=600):
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.monip=monip
        self.parent=parent
        self.modele=None
        self.nom=None
        self.largeur=largeur
        self.hauteur=hauteur
        self.images={}
        self.modes={}
        self.modecourant=None
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadrelogin)
        
    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.pack_forget()
        self.modecourant=cadre
        self.modecourant.pack(expand=1,fill=BOTH)            

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            self.cadreactif.pack_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.pack(expand=1,fill=BOTH)
        else:
            self.cadreactif.pack()
    
    def chargercentral(self,repmodules, repoutils):
        for i in repmodules:
            self.listemodules.insert(END,i)
        for i in repoutils:
            self.listeoutils.insert(END,i)
        self.changecadre(self.cadrecentral)
        
    def creercadres(self):
        self.creercadrelogin()
        self.creercadrecentral()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
                
    def creercadrelogin(self):
        self.cadrelogin=Frame(self.root)
        self.canevalogin=Canvas(self.cadrelogin,width=640,height=480,bg="grey")
        self.canevalogin.pack()
        self.lbltitre=Label(self.cadrelogin, text="Connexion")
        self.orglogin=Entry(bg="white")
        self.orglogin.insert(0, "CVM")
        self.lblorgnom=Label(self.cadrelogin, text="Nom de l'organisation")
        self.nomlogin=Entry(bg="white")
        self.nomlogin.insert(12, "jmd")
        self.lblnom=Label(self.cadrelogin, text="Nom de l'usager")
        btnconnecter=Button(text="Connecter au serveur",bg="pink",command=self.loginclient)
        self.canevalogin.create_window(300,160, window=self.lblorgnom, width=175, height=30)
        self.canevalogin.create_window(300,200,window=self.orglogin,width=175,height=30)
        self.canevalogin.create_window(300,260, window=self.lblnom, width=175, height=30)
        self.canevalogin.create_window(300,300,window=self.nomlogin,width=175,height=30)
        self.canevalogin.create_window(300,400,window=btnconnecter,width=175,height=30)
        
    
    def creercadrecentral(self):
        self.cadrecentral=Frame(self.root)
        self.cadremodule=Frame(self.cadrecentral)
        self.canevamodule=Canvas(self.cadremodule,width=640,height=480,bg="green")
        self.canevamodule.pack()
        
        self.listemodules=Listbox(self.cadremodule,bg="lightblue",borderwidth=0,relief=FLAT,width=40,height=6)
        self.ipcentral=Entry(bg="pink")
        self.ipcentral.insert(0, self.monip)
        btnconnecter=Button(text="Choisir un module",bg="pink",command=self.requetemodule)
        self.canevamodule.create_window(200,100,window=self.listemodules)
        self.canevamodule.create_window(200,450,window=btnconnecter,width=100,height=30)
        self.cadremodule.pack(side=LEFT)
        # Autre cadre
        
        self.cadreoutils=Frame(self.cadrecentral)
        self.canevaoutils=Canvas(self.cadreoutils,width=640,height=480,bg="green")
        self.canevaoutils.pack()
        
        self.listeoutils=Listbox(self.cadreoutils,bg="lightblue",borderwidth=0,relief=FLAT,width=40,height=6)
        btnconnecter=Button(text="Choisir un outils",bg="pink",command=self.requeteoutil)
        self.canevaoutils.create_window(200,100,window=self.listeoutils)
        self.canevaoutils.create_window(200,450,window=btnconnecter,width=100,height=30)
        self.cadreoutils.pack(side=LEFT)
        
        
    def requetemodule(self):
        mod=self.listemodules.selection_get()
        if mod:
            self.parent.requetemodule(mod)
            
    def requeteoutil(self):
        mod=self.listeoutils.selection_get()
        if mod:
            self.parent.requeteoutils(mod)
        
    def loginclient(self):
        ipserveur=self.monip##self.ipsplash.get() # lire le IP dans le champ du layout
        nom=self.nomlogin.get() # noter notre nom
        self.parent.loginclient(ipserveur,nom)
        
    def center(toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
                
    def fermerfenetre(self):
        # Ici, on pourrait mettre des actions a faire avant de fermer (sauvegarder, avertir, etc)
        self.parent.fermefenetre()
##Conserver pour le chargement d'images
    #def chargeimages(self):
      #  im = Image.open("./images/chasseur.png")
        #self.images["chasseur"] = ImageTk.PhotoImage(im)

    
if __name__ == '__main__':
    m=Vue(0,"jmd","127.0.0.1")

    m.root.mainloop()
    