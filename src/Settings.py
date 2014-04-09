# -*- coding: utf-8 -*-

import curses
from curses import KEY_UP, KEY_DOWN


curses.initscr()
win = curses.newwin(30,70,0,0)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(0)


def askSetting(input):
    name = "Player1"
    difficulty = 2
    levelNumber = 1
    if input == "playerName":
        name = askName()
    elif input == "difficulty":
        difficulty = askDifficulty()
    elif input == "levelNumber":
        levelNumber = askLevelNumber()

    settings = {'playerName' : name, 'difficulty' : difficulty, 'levelNumber' : levelNumber}

def askName():
    win.clear()
    curses.echo()
    win.addstr(10,20,"Comment t'appelles-tu ?")
    name = win.getstr(11,20)
    curses.noecho()
    return name

def askDifficulty():
    win.clear()
    win.addstr(10,20,"Choisis ta difficulté")
    menuCursor = 0
    key = 0
    while key != 27:

        if menuCursor == 0:
            win.addstr(11,20,"[1 : Facile]    ")
        else:
            win.addstr(11,20,"1 : Facile    ")
        if menuCursor == 1:
            win.addstr(12,20,"[2 : Normal]    ")
        else:
            win.addstr(12,20,"2 : Normal    ")
        if menuCursor == 2:
            win.addstr(13,20,"[3 : Difficile]    ")
        else: 
            win.addstr(13,20,"3 : Difficile    ")
        
        key = win.getch()
        if key  == ord('z'):
            if menuCursor != 0:
                menuCursor -= 1
        if key == ord('s'):
            if menuCursor != 2:
                menuCursor += 1
        if key == ord('e'):
            difficulty = menuCursor+1
            return difficulty

def askLevelNumber():
    win.clear()
    numberOfLevels = 12
    curses.echo()
    win.addstr(10,20,"Quel niveau veux-tu jouer ? ")
    for i in range(numberOfLevels):
        while i < 5:
            win.addstr(10,20+i,i)
        while 5 <= i < 10:
            win.addstr(11,15+i,i)
        while 10 <= i < 15:
            win.addstr(12,10+i,i)
    levelNumber = win.getstr(13,20)
    curses.noecho()
    return levelNumber


if __name__ == '__main__':
    settings = askSesttings()
    print settings
    