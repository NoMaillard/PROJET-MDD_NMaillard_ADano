import curses
import random
import logging

import Level
import Snake


def create(menu, level, snake, food, win, state, name, difficulty):
    return {
        'menu': menu,
        'level': level,
        'snake': snake,
        'food': food,
        'win': win,
        'state': state,
        'name': name,
        'difficulty': difficulty}


def show(game):
    win = getWin(game)
    food = getFood(game)
    level = getLevel(game)
    snake = getSnake(game)
    win.erase()
    Level.show(level, win)
    Snake.show(snake, win)
    win.addstr(food[1], food[0], 'X')
    return


def interact(game):
    snake = getSnake(game)
    food = getFood(game)
    win = getWin(game)
    key = win.getch()
    win.timeout(200)
    if foodEaten(snake, food):
        game = setNewFood(game)
    newSnake = Snake.computeNextPos(key, snake, food, win)
    if newSnake == 'quitProgram':
        setState('quitProgram', game)
    else:
        game = setSnake(newSnake, game)
    return


def quitGame(status, game):
    if status == 'quitProgram':
        setState(status, game)
    return


def getMenu(game):
    # retourne la variable menu
    return game['menu']


def getLevel(game):
    # retourne la variable level
    return game['level']


def setLevel(level, game):
    # change la variable level dans le game
    game['level'] = level
    return game


def getSnake(game):
    return game['snake']


def setSnake(snake, game):
    game['snake'] = snake
    return game


def getFood(game):
    return game['food']


def setNewFood(game):
    level = getLevel(game)
    win = getWin(game)
    logging.info('food : ' + str(game['food']))
    newFoodX = random.randint(1, Level.getWidth(level))
    newFoodY = random.randint(1, Level.getHeight(level))
    while win.inch(newFoodY, newFoodY) != ord(' '):
        newFoodX = random.randint(1, Level.getWidth(level))
        newFoodY = random.randint(1, Level.getHeight(level))
    game['food'] = [newFoodX, newFoodY]
    return game


def foodEaten(snake, food):
    if food[0] == Snake.getHeadX(snake) and food[1] == Snake.getHeadY(snake):
        return True
    else:
        return False


def getState(game):
    # retourne l'etat du game
    return game['state']


def setState(state, game):
    game['state'] = state
    return game


def getWin(game):
    # retourne la fenetre du jeu
    return game['win']


def getName(game):
    # retourne le nom du joueur
    return game['name']


def setName(name, game):
    # change le nom du joueur
    game['name'] = name
    return game


def askName(game):
    # demande a l'utilisateur le nom du joueur
    win = game['win']
    win.erase()
    curses.echo()
    win.addstr(10, 20, "What's your name ?")
    name = win.getstr(11, 20)
    curses.noecho()
    return name


def getDifficulty(game):
    # retourne la difficulte
    return game['difficulty']


def setDifficulty(difficulty, game):
    # change la difficulte
    game['difficulty'] = difficulty
    return game


def askDifficulty(game):
    # demande la difficulte a l'utilisateur
    win = game['win']
    win.erase()
    curses.echo()
    difficulty = 0
    while difficulty < 1 or difficulty > 3:
        win.addstr(10, 20, "Choose your difficulty")
        win.addstr(11, 20, "1 : Easy, 2 : Medium, 3 : Hard")
        try:
            difficulty = int(win.getstr(12, 20))
            if difficulty < 1 or difficulty > 3:
                raise ValueError()
        except ValueError:
            win.erase()
            win.addstr(13, 20, "retry !")
    curses.noecho()
    return difficulty
