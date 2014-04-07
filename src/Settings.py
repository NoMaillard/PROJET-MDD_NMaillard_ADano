# -*- coding: utf-8 -*-

import sys

def askSesttings():
    name = askName()
    difficulty = askDifficulty()
    levelNumber = askLevelNumber()

    settings = {"name" : name,"difficulty" : difficulty, "levelNumber" : levelNumber}
    return settings

def askName():
    name = raw_input("Comment t'appelles-tu ?\n")
    return name

def askDifficulty():

    sys.stdout.write("Choisis ta difficulté\n")
    sys.stdout.write("1 : Facile\n")
    sys.stdout.write("2 : Normal\n")
    sys.stdout.write("3 : Difficile\n")
    difficulty = raw_input("Difficulté :")
    difficulty = int(difficulty)

    return difficulty

def askLevelNumber():

    levelNumber = raw_input("Quel niveau veux-tu jouer ?")
    return levelNumber


if __name__ == '__main__':
    settings = askSesttings()
    print settings
