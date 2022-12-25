class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def cri(self, cri):
        return print(cri)

class Chat(Animal):
    def cri(self):
        print(type(self).__name__, self.nom, "a milaulé : Miaou!")

class Chien(Animal):
    def cri(self):
        print(type(self).__name__, self.nom,"a aboyé: Ouaf Ouaf!" )
    
class Ferme:
    def __init__(self, animaux =[]):
        self.animaux = animaux
    def ajouter_animal(self, animal):
        self.animaux.append(animal)
    def get_nb_animaux(self):
        return len(self.animaux)
    def __str__(self):
        return "La ferme contient " + str(self.get_nb_animaux()) + " animaux."

