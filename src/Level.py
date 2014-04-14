<<<<<<< HEAD
#!/usr/bin/python
=======
# -*- coding: utf-8 -*-
>>>>>>> FETCH_HEAD
import Settings
import sys
import curses
<<<<<<< HEAD
=======


curses.initscr()
win = curses.newwin(30, 80, 0, 0)
curses.noecho()
curses.curs_set(0)
curses.cbreak()
win.keypad(1)
win.nodelay(0)





>>>>>>> FETCH_HEAD

curses.initscr()
win = curses.newwin(20,80,0,0)
curses.noecho()
curses.curs_set(0)
win.nodelay(0)

def main():
<<<<<<< HEAD
    m = create(1)
    show(m)
    return
=======
    niveau = dict()
    niveau = create(niveau, 4)
    show(niveau)
    char = win.getch()







def getLevelNumber(level):
    return level["number"]
    



def setLevelNumber(level, nb):
    level["number"] = nb
    return level


>>>>>>> FETCH_HEAD



def show(level):
<<<<<<< HEAD
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
=======
    assert type(level["map"]) is list

    # affiche le niveau
    ln = 0
    for i in level["map"] :
        ligne = ""
        for caractere in i :
            ligne = ligne + caractere
        win.addstr(ln, 0, ligne)
        ln += 1
        win.refresh()
    return





def create(level, mapNumber):
    assert type(mapNumber) is int
       

    # recupere l'ensemble des cartes
    fichier = open('maps.txt', 'r')
    chaine = fichier.read()

        
    # separation des cartes
    allMaps = chaine.split("map\n")
    # test carte demandee existante
    if mapNumber < len(allMaps):
        # separation des lignes de la carte demandee
        level["map"] = list(allMaps[mapNumber].split("\n"))
        return level
    else:
        win.addstr("Error\n mapNumber > len(allMaps)\n")
    return level
>>>>>>> FETCH_HEAD
                


if __name__ == "__main__" :
    main()
<<<<<<< HEAD
=======
    curses.echo()
    curses.nocbreak()
    win.keypad(0)
    curses.endwin()



>>>>>>> FETCH_HEAD

