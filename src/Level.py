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
        level['level'] = list(level['allLevels'][levelNumber].split("\n"))
    return level


def getLevel(level):
    return level['level']


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
    win.erase()
    curses.echo()
    levelNumber = 0
    while levelNumber < 1 or levelNumber > len(level['allLevels']):
        max = str(len(level['allLevels']))
        win.addstr(10, 20, "Choose your level [ 1 - " + max + " ]")
        try:
            levelNumber = int(win.getstr(11, 20))
            if levelNumber < 1 or levelNumber > len(level['allLevels']):
                raise ValueError()
        except ValueError:
            win.erase()
            win.addstr(12, 20, "retry !")
    curses.noecho()
    return levelNumber


def getNumberOfLevels(level):
    # retourne le nombre de niveaux
    return len(level['allLevels'])


def show(level, win):
    win.erase()
    currentLevel = getLevel(level)
    for i in range(len(currentLevel)):
        win.addstr(i, 0, currentLevel[i])
    return


def getWidth(level):
    return 67


def getHeight(level):
    return 20
