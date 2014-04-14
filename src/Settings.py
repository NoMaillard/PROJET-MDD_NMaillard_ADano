#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses



def create(name,levelNumber,difficulty):
    curses.initscr()
    win = curses.newwin(20,80,0,0)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(0)
    

def askSetting(input,settings):
    if input == "playerName":  
        settings['playerName'] = askName()
        return settings
    elif input == "difficulty":
        settings['difficulty'] = askDifficulty()
        return settings
    elif input == "levelNumber":
        settings['levelNumber'] = askLevelNumber()
        return settings

def askName():
    win.erase()
    win.border(0)
    curses.echo()
    win.addstr(10,20,"Comment t'appelles-tu ?")
    name = win.getstr(11,20)
    curses.noecho()
    return name

def askDifficulty():
    win.erase()
    win.border(0)
    menuCursor = 0
    key = 0
    
    while key != 27:
        win.erase()
        win.border(0)
        win.addstr(10,20,"Choisis ta difficulté")
        if menuCursor == 0:
            win.addstr(11,20,"->1 : Facile    ")
        else:
            win.addstr(11,22,"1 : Facile    ")
        if menuCursor == 1:
            win.addstr(12,20,"->2 : Normal    ")
        else:
            win.addstr(12,22,"2 : Normal    ")
        if menuCursor == 2:
            win.addstr(13,20,"->3 : Difficile    ")
        else: 
            win.addstr(13,22,"3 : Difficile    ")

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
    win.border(0)
    numberOfLevels = 12
    curses.echo()
    levelNumber = -1
    while levelNumber < 0 or levelNumber > numberOfLevels:
        win.border(0)
        try:
            win.addstr(10,20,"Quel niveau veux-tu jouer ? [1 - "+str(numberOfLevels)+"]")
            levelNumber = int(win.getstr(11,20))
            win.erase()
            if levelNumber < 0 or levelNumber > numberOfLevels:
                win.addstr(12,20,"retry !")
        except ValueError:
            win.erase()
            win.addstr(12,20,"retry !")
    curses.noecho()
    return levelNumber


if __name__ == '__main__':
    askSetting("playerName")
    askSetting("difficulty")
    askSetting("levelNumber")
    print settings
    