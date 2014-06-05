#!/usr/bin/python

# -*- coding: utf-8 -*-

import curses

import Game


def create(levelNumber, levelFile):
    # cree la variable de type level

    # recupere l'ensemble des niveaux
    fichier = open(levelFile, 'r')
    chaine = fichier.read()
    level = dict()

    # separation des niveaux en niveaux individuels
    level['allLevels'] = chaine.split("level\n")
    level['number'] = levelNumber

    # test existance du niveau demande
    if levelNumber <= len(level['allLevels']):
        # separation en lignes du niveau demande
        level['map'] = list(level['allLevels'][levelNumber-1].split("\n"))
    return level


def getMap(level):
    return level['map']


def getLevelNumber(level):
    # retourne le numero du niveau en cours
    return level['number']


def setLevelNumber(number, level):
    # change le numero du niveau
    level['number'] = number
    return level


def askLevelNumber(game):
    # demande le numero du niveau a l'utilsateur
    win = Game.getWin(game)
    level = Game.getLevel(game)
    win.nodelay(0)
    win.erase()
    curses.echo()
    curses.curs_set(1)
    levelNumber = 0
    while levelNumber < 1 or levelNumber > len(level['allLevels']) - 1:
        max = str(getNumberOfLevels(level)-1)
        win.addstr(10, 20, "Choose your level [ 1 - " + max + " ]")
        try:
            levelNumber = int(win.getstr(11, 20))
            if levelNumber < 1 or levelNumber > len(level['allLevels']) - 1:
                raise ValueError()
        except ValueError:
            win.erase()
            win.addstr(12, 20, "retry !")
    curses.noecho()
    curses.curs_set(0)
    return levelNumber


def getNumberOfLevels(level):
    # retourne le nombre de niveaux
    return len(level['allLevels'])


def show(level, win):
    currentLevel = getMap(level)
    for i in range(len(currentLevel)):
        win.addstr(i, 0, currentLevel[i])
    return


def getWidth(level):
    return 67


def getHeight(level):
    return 20
