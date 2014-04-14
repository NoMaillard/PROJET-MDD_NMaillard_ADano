# -*- coding: utf-8 -*-
import Settings
import Coin
import sys
import curses


curses.initscr()
win = curses.newwin(30, 80, 0, 0)
curses.noecho()
curses.curs_set(0)
curses.cbreak()
win.keypad(1)
win.nodelay(0)







def main():
    niveau = dict()
    niveau = create(niveau, 4)
    show(niveau)
    char = win.getch()







def getLevelNumber(level):
    return level["number"]
    



def setLevelNumber(level, nb):
    level["number"] = nb
    return level





def show(level):
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
                


if __name__ == "__main__" :
    main()
    curses.echo()
    curses.nocbreak()
    win.keypad(0)
    curses.endwin()




