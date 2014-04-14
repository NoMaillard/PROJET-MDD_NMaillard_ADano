import Settings
import Coin
import sys
import curses


win = curses.newwin(20, 80, 0, 0)
curses.initscr()
curses.noecho()
curses.keypad(1)



def main():
        m = create(4)
        show(m)








def show(level):
        assert type(level) is list
        
	# affiche le niveau
        for i in level :
                ligne = ""
                for caractere in i :
                        ligne = ligne + caractere
                win.addstr(ligne)
                win.addstr("\n")
                
        return
	
	
def create(mapNumber):
        assert type(mapNumber) is int
        
	
	# recupere l'ensemble des cartes
        fichier = open('maps.txt', 'r')
        chaine = fichier.read()

        
	# separation des cartes
        allMaps = chaine.split("map\n")
	
	# test carte demandee existante
        if mapNumber < len(allMaps):
                # separation des lignes de la carte demandee
                level = list(allMaps[mapNumber].split("\n"))
                return level
        else:
                win.addstr("Error\n mapNumber > len(allMaps)\n")
                return
                
	


if __name__ == "__main__" :
        main()

	
	
	
