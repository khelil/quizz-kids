from browser import document
from browser.html import document
document <= ("HTML.html")

def click(ev):
    document <= html.button
    document["Bouton1"].bind("click", click)
    print("Hello")


 











import csv
from array import array
from math import sqrt

# transforme Caracteristiques_des_persos.csv en tableau
# retourne le tableau
def get_csv_caracteristics():
    persos = []
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
            persos.append(dico_2)
    return persos

# transforme Characters.csv en tableau
# retourne le tableau
def get_csv_persos():
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
    return persos

# change l'index du tableau persos_caracteristics
# retourne un dictionnaire
def change_index_by_name_caracteristics(persos: array):
    persos_index_name = {}
    for element in persos:
        persos_index_name[element['Name']] = {'Courage':element['Courage'],'Ambition':element['Ambition'],'Intelligence':element['Intelligence'],'Good':element['Good']}
    return persos_index_name

# change l'index du tableau persos
# retourne un dictionnaire
def change_index_by_name_persos(persos: array):
    persos_index_name = {}
    for element in persos:
        persos_index_name[element['Name']] = {'House':element['House']}
    return persos_index_name

# fusionne les deux dictionnaires
# retourne un dictionnaire
def merge_by_name(persos: dict, caracteristics: dict):
    merged_persos = {}
    for name_perso in persos:
        for name_caracteristic in caracteristics:
            if name_perso == name_caracteristic:
                merged_persos[name_perso] = persos[name_perso].copy()
                merged_persos[name_perso].update(caracteristics[name_perso])
    return merged_persos

# calcul la distance euclidienne entre deux persos
# retourne la distance
def calc_distance(perso1: dict, perso2: dict):
    return sqrt((int(perso1['Courage']) - int(perso2['Courage']))**2)\
            + ((int(perso1['Ambition']) - int(perso2['Ambition']))**2)\
            + ((int(perso1['Intelligence']) - int(perso2['Intelligence']))**2)\
            + ((int(perso1['Good']) - int(perso2['Good']))**2)
        
# calcul la distance euclidienne entre un perso inconnu
# et la liste des persos d'un dict
# retourne un nouveau dict avec une prop distance
def ajout_distance(persos, perso_inconnu):
    for perso_name in persos:
        persos[perso_name]['Distance'] = calc_distance(perso_inconnu, persos[perso_name])
    return persos

# renvoi la liste des kppv
# retourne un tableau
def kppv(liste: dict, nbre_voisin):
    nbre_voisin = int(nbre_voisin)
    liste_voisins = []
    voisins = sorted(liste.items(), key=lambda x: x[1]['Distance'])
    for nbre_voisin in range(0, nbre_voisin):
        liste_voisins.append(voisins[nbre_voisin])
    return liste_voisins

# renvoi la meilleure distance
def meilleur_distance(persos):
    distances = {}
    for name, perso in persos:
        distance = int(perso['Distance'])
        if distance in distances :
            distances[distance] += 1
        else:
            distances[distance] = 1
    max = 0
    for distance, nb in distances.items():
        if nb > max: 
            max = nb
            best_distance = distance
    return best_distance 

def launch(perso_inconnu, nbre_voisin):

    persos_caracteristics = get_csv_caracteristics()
    persos_caracteristics = change_index_by_name_caracteristics(persos_caracteristics)

    persos = get_csv_persos()
    persos = change_index_by_name_persos(persos)

    persos_merged = merge_by_name(persos,persos_caracteristics)

    persos_distance_inconnu = ajout_distance(persos_merged,perso_inconnu)

    liste_voisins = kppv(persos_distance_inconnu, nbre_voisin)
    print("Liste des voisins : ")
    print(liste_voisins)

    best_distance = meilleur_distance(liste_voisins)
    print("Meilleure distance : ")
    print(best_distance)

#launch()
