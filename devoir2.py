#coding : utf-8

import csv

# Définir l'emplacement du fichier et le relier à la variable «fichier»:
fichier = "concordia1.csv"

# Déclaration des variables: 
tampon = ""
ligne = 0
type = ""
nbPages = ""
longTitre = 0
nom = ""
prenom = ""
titre = ""


#Ouvrir le fichier :
f = open(fichier)

# Définir la variable «lignes», qui va permettre de lire le fichier:
lignes = csv.reader(f)

# Ajouter la fonction «next» pour commencer à la deuxième ligne :
next(lignes) 

# Créer la boucle qui va parcourir chacune des lignes et récupérer les informations nécessaires:
for ligne in lignes :
    
    # Afficher la longeur du titre de chaque thèse ou mémoire:
    longTitre = len(ligne[2])
    
    # Afficher s'il s'agit d'une thèse ou d'un mémoire:
    tampon = ligne[6]
    if("Theses" in tampon):
         type = "thèse"
    else:
        type = "mémoire"
    
    # Afficher les informations disponibles sur le nombre de pages de la thèse ou du mémoire (** Voir commentaires en bas**) : 
    tampon = ligne[5]
    lensTampon = tampon.split(";")
    nbPages = lensTampon[0]
    nbPages =nbPages.replace("leaves",'')
    nbPages =nbPages.replace(": ill.",'')
    nbPages = nbPages.strip()
    
    # Afficher les autres informations nécessaires:
    nom = ligne[0]
    prenom = ligne[1]  
    titre = ligne[2]
    
    # Affichage final de l'ensemble des informations : 
    print("La" + " " + type + " de " + prenom + " " + nom + " compte", nbPages, " pages" + ". Son titre est " + titre + " (", longTitre ,  " caractères).")
    

# Commentaires au sujet du total de nombre de pages : 

# Puisque je n'ai pas réussi à trouver un moyen de calculer le nombre total de pages de chacun des documents, j'ai opté pour afficher
# l'ensemble des informations disponibles concernant le nombre de pages, soit les chiffres romains (s'il y a lieu) et le nombre de pages (en chiffres numériques).

# Pour parvenir à additionner les chiffres romains aux chiffres numériques, il aurait fallu faire pour chaque cas possible des «if» et «else», afin de
# transformer les chiffres romains en chiffres numériques.Par la suite, il aurait fallu additionner (lorsque c'est le cas) les chiffres romains,transformés en chiffres
# numériques, avec les chiffres numériques. 
