import os
import csv
from Ferme import Ferme
from Ferme import Chien
from Ferme import Chat

clear = lambda: os.system('cls')
   
exitedMenu = False
maferme = Ferme()
 
# Script du Menu
while(exitedMenu == False):
    print("\n[1] pour Ajouter un animal,[2] Lancer le cri des animaux, [3] Tuer un animal, [4] Voir le nombre d'animaux, [5] pour Quitter")
    print("________________")

    selectedOption = str(input("Choisissez une option : "))
    print(selectedOption)
    
    # Choix listage des personnes
    if(selectedOption== "1"):
        clear()
        print("| Ajout d'un nouvel animal |")
        print("[1] pour Chat ou [2] pour Chien")
        option = 0
        while option != "1" and option != "2":
            option = str(input("Choisissez une option : "))
            
        nom = str(input("Entrez un nom : "))
        age = str(input("Entrez un âge : "))
        if option == "1" :
            nouveau = Chat(nom,age)
        elif option == "2":
            nouveau = Chien(nom,age)
        clear()
        maferme.ajouter_animal(nouveau)
                

    # Choix ajout d'une personne
    elif(selectedOption == "2"):
        clear()
        print("| Cris des animaux |")
        maferme.crier()

                        
    # Choix édition d'une personne
    elif(selectedOption =="3"):
        clear()
        print("| Meurtre d'un animal |")
        nom_animal = ""
        if(maferme.contient_animaux()):
            while(nom_animal == ""):
                maferme.get_noms()
                nom_animal = str(input("Entrez le nom de l'animal à tuer : "))
                if nom_animal != "":
                    clear()
                    killed = maferme.tuer(nom_animal)
                    if killed == False:
                        print("Aucun animal trouvé")
                else:
                    print("Renseignez un nom")
        else:
            print("Aucun animal à tuer")
        

    # Choix suppression d'une personne
    elif(selectedOption == "4"):
        clear()
        print("| Voir le nombre d'animaux |")    
        print(maferme)    
            
    # Choix sortie programme
    elif(selectedOption == "5"):
        clear()
        break;

    # Choix incorrecte
    else:
        clear()
        print("Option incorrecte")
    

print("Fin du programme")