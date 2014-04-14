#!/usr/bin/python
import Settings
import sys
import curses

curses.initscr()
win = curses.newwin(20,80,0,0)
curses.noecho()
curses.curs_set(0)
win.nodelay(0)

def main():
    m = create(1)
    show(m)
    return



def show(level):
    # assert type(level) is list
	# affiche le niveau
    lineNumber = 0
    for i in level :
        win.addstr(lineNumber,0,i)
        lineNumber += 1
    return
	
	
def create(levelNumber):
	# recupere l'ensemble des niveaux
    fichier = open('levels.txt', 'r')
    chaine = fichier.read()

        
    # separation des niveaux
    allLevels = chaine.split("level\n")
	
	# test carte demandee existante
    if levelNumber < len(allLevels):
        # separation des lignes de la niveau demandee
        level = list(allLevels[levelNumber].split("\n"))
        return level
    else:
        win.addstr(5,20,"Error\n levelNumber > len(allLevels)\n")
        return
                
	


if __name__ == "__main__" :
    main()

	
	
	
