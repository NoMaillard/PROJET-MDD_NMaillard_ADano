#!/usr/bin/python
import logging

import Game
import Level
import HighScores


def create(*argv):
    # cree un menu en fonction des arguments
    menuCursor = 0
    selectedItem = -1
    menuItems = []
    j = 0
    for i in argv:
        menuItems.append(i)
        j += 1
    menu = {'items': menuItems,
            'cursor': menuCursor,
            'selectedItem': selectedItem}
    return menu


def show(game):
    # affiche le menu
    menu = Game.getMenu(game)
    win = Game.getWin(game)
    win.erase()
    for i in range(len(menu['items'])):
        if i == menu['cursor']:
            win.addstr(10 + i, 20, "->" + str(menu['items'][i]))
        else:
            win.addstr(10 + i, 22, str(menu['items'][i]))
    win.addstr(2, 2, 'Name : ' + str(Game.getName(game)))
    win.addstr(3, 2, 'Difficulty : ' + str(Game.getDifficulty(game)))
    win.addstr(4, 2, 'Level : ' +
               str(Level.getLevelNumber(Game.getLevel(game))))
    return


def interact(game):
    # interaction entre l'utilisateur et le menu
    menu = Game.getMenu(game)
    win = Game.getWin(game)
    # deplacement du curseur
    menu['selectedItem'] = -1
    key = win.getch()
    if key == ord('z'):
        if menu['cursor'] != 0:
            menu['cursor'] -= 1
    if key == ord('s'):
        if menu['cursor'] != len(menu['items']) - 1:
            menu['cursor'] += 1
    if key == ord('e'):
        menu['selectedItem'] = menu['cursor']
    # action a effectuer en fonction de l'item selectionne
    if menu['selectedItem'] == 0:
        game = Game.setName(Game.askName(game), game)
    if menu['selectedItem'] == 1:
        game = Game.setDifficulty(Game.askDifficulty(game), game)
    if menu['selectedItem'] == 2:
        newLevel = Level.create(Level.askLevelNumber(game), 'levels.txt')
        logging.info("nouveau niveau : " + str(newLevel))
        game = Game.setLevel(newLevel, game)
    if menu['selectedItem'] == 3:
        HighScores.show(HighScores.get(), win)
    if menu['selectedItem'] == 4:
        Game.setState('game', game)
    if menu['selectedItem'] == 5:
        Game.setState('quitProgram', game)
    if menu['selectedItem'] == 6:
        Game.setState('editor', game)
    return


def getNumberOfMenuItems(menu):
    # retourne le nombre d'items dans le menuce
    return len(menu['items'])
