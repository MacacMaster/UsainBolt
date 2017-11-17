import sqlite3
import random

# Création d'un objet connect "database" à une base de donnée "fightus"
database = sqlite3.connect('SprintMasterData.db')

# Création d'un curseur pour cette base de donnée
curseur = database.cursor()

# Creer une table si elle n'existe pas
curseur.execute('''CREATE TABLE IF NOT EXISTS organisation
             (id integer, nomOrganisation text, nomUsager, motDePasse text)''')

# Supprimer tout ce qui se trouve dans la bd
for comptes in curseur.execute('SELECT id FROM organisation'):
    curseur.execute('DELETE FROM organisation')
    
# Ajouter les nouveaux comptes
curseur.execute("INSERT INTO organisation VALUES ('1', 't', 't', 't')")

# Voir les objets de la bd
for comptesOrg in curseur.execute('SELECT * FROM organisation'):
    print(comptesOrg)

# Sauvegarder (commit) les changements
database.commit()

# Fermer la connection a la bd
database.close()