class Animal:
    def __init__(self, nom, age=0):
        self.nom = nom
        self.age = age

    def cri(self, cri):
        return print(cri)

class Chat(Animal):
    def cri(self):
        print(type(self).__name__, self.nom, "a milaulé : Miaou!")
    def __del__(self):
        print(type(self).__name__, self.nom,"a été assassiné!" )

class Chien(Animal):
    def cri(self):
        print(type(self).__name__, self.nom,"a aboyé: Ouaf Ouaf!" )
    def __del__(self):
        print(type(self).__name__, self.nom,"a été assassiné!" )
    
class Ferme:
    def __init__(self, animaux =[]):
        self.animaux = animaux
        print("La ferme a été créé !" )
        
    def __del__(self):
        print("La ferme a été détruite !" )
    
    def contient_animaux(self):
        if len(self.animaux)>0:
            return True
        return False
        
    def get_noms(self):
        if self.contient_animaux():
            for animal in self.animaux:
                print(animal.nom)
        else:
            print("Aucun animal")
            
    def get_nb_animaux(self):
        return len(self.animaux)
    
    def ajouter_animal(self, animal):
        self.animaux.append(animal)
        print(type(animal).__name__, animal.nom,"est né!" )
        
    def crier(self):
        if self.contient_animaux():
            for animal in self.animaux:
                animal.cri()
        else:
            print("Aucun animal n'a crié")
            
    def tuer(self,nom):
        killed = False
        for i in range(len(self.animaux)):
            if self.animaux[i].nom == nom:
                del self.animaux[i]
                return True
        return killed
    
    def __str__(self):
        return "La ferme contient " + str(self.get_nb_animaux()) + " animaux."
    

