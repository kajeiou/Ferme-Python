class Animal:
    def __int__(self, nom, age):
        self.nom = nom
        self.age = age
    def cri(self, cri):
        return print(cri)

class Chat(Animal):
    def cri(self, cri):
        cri = "Miaou"
        print(cri)

class Chien(Animal):
    def cri(self, cri):
        cri = "Ouaf"
        print(cri)

class Ferme():
    def __int__(self, animaux):
        self.animaux = animaux
    def ajouter_animal(self, animal):
        self.animaux.append(animal)
    def nbAnimaux(self):
        return len(self.animaux)

