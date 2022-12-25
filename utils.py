from Ferme import Ferme
from Ferme import Chien
from Ferme import Chat

chien1 = Chien("Pitbull",5)
chien1.cri()
chat1 = Chat("Milou",4)
chat1.cri()
maferme = Ferme([chien1,chat1])
maferme.ajouter_animal(Chien("Berger Allemand", 4))
maferme.get_nb_animaux()
print(maferme)