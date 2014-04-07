import Settings
import Coin




def create(setting):
	map = mapCreate(setting["levelNumber"])
	# charge la carte du fichier dans la variable
	
	
	
	return map
	
	

def show(level):
	# affiche le niveau
	
	
	
	
	
def mapCreate(mapNumber):
	
	# recupere l'ensemble des cartes
	fichier = open(maps.txt, "r")
	chaine = fichier.read()
	
	# separation des cartes
	allMaps = chaine.split("map\n")
	
	# test carte demandee existante
	if mapNumber <= len(allMaps):
		# separation des lignes de la carte demandee
		map = allMaps[mapNumber].split("\n")
	

	
	
	
	
