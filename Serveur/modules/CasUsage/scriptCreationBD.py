import sqlite3
import random

# Création d'un objet connect "database" à une base de donnée "fightus"
database = sqlite3.connect('cas.db')

# Création d'un curseur pour cette base de donnée
curseur = database.cursor()
# Creer une table si elle n'existe pas

curseur.execute('''CREATE TABLE CasUsage (Id integer,Description text ,Etat text,ScenarioUtilisation_Id integer)''')
curseur.execute('''CREATE TABLE ScenarioUtilisation (Id integer,Actions text,ProchaineAction integer,ScenarioUtilisation_Id integer)''')


# Supprimer tout ce qui se trouve dans la bd
#for comptes in curseur.execute('SELECT id FROM client'):
  #  curseur.execute('DELETE FROM client')
    
# Ajouter les nouveaux comptes
#curseur.execute("INSERT INTO client VALUES ('1', 'Cas1', 'Actif')")
#curseur.execute("INSERT INTO client VALUES ('2', 'Cas2', 'NonActif')")

# Voir les objets de la bd
#for comptes in curseur.execute('SELECT * FROM client'):
   # print(comptes)

# Sauvegarder (commit) les changements
database.commit()

# Fermer la connection a la bd
database.close()