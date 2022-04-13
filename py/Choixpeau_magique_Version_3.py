import csv
from math import sqrt

persos_caracteristiques = []
with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(";")
    for line in lines[1:]:
        line = line.strip()
        values = line.split(';')
        dico_2 = {}
        for i in range(len(keys)):
            dico_2[keys[i]] = values[i]
        persos_caracteristiques.append(dico_2)


persos = []
with open("Characters.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(";")
    for line in lines[1:]:
        line = line.strip()
        values = line.split(';')
        dico_1 = {}
        for i in range(len(keys)):
            dico_1[keys[i]] = values[i]
        persos.append(dico_1)

#print(persos)

index_perso_prenom = {}
for element in persos:
    index_perso_prenom[element['Name']] = {'House':element['House']}

#print(index_perso_prenom)

# transformer en fonction 
# def change_index change l'index du tableau


index_caracteristiques_prenom = {}
for element in persos_caracteristiques:
        index_caracteristiques_prenom[element['Name']] = {'Courage':element['Courage'],'Ambition':element['Ambition'],'Intelligence':element['Intelligence'],'Good':element['Good']}

#print(index_caracteristiques_prenom)

index_perso_caracteristiques = {}
for name_perso in  index_perso_prenom:
    for name_caracteristiques in index_caracteristiques_prenom:
        if name_perso == name_caracteristiques:
            index_caracteristiques_prenom[name_perso].update(index_perso_prenom[name_perso])
            
print(index_caracteristiques_prenom)



def distance(perso1: dict, perso2: dict):
        return sqrt((perso1['Courage'] - perso2['Courage'])**2)\
            + ((perso1['Ambition'] - perso2['Ambition'])**2)\
            + ((perso1['Intelligence'] - perso2['Intelligence'])**2)\
            + ((perso1['Good'] - perso2['Good'])**2)
  


def ajout_distance(tab, perso_inconnu):
    for inconnu in tab:
        inconnu['Distance'] = distance(perso_inconnu, inconnu)
    return tab

liste_voisins = []
def kppv(voisins: list, liste1: list):
    voisins = sorted(liste1['Distance'])
    k = int(input("Combien de voisins afficher?  "))
    for k in range (0,k):
        liste_voisins.append(liste1[k])


def meilleur_distance(tab):
    distances = {}
    for voisins in tab:
        if voisins['Distance'] in distances :
            distances[voisins['Distance']] += 1
        else : 
            distances[voisins['Distance']] = 1
    max = 0
    for distance, nb in distances.items():
        if nb > max: 
            max = nb
            best_distance = distance
        return best_distance 