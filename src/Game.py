import curses
import random
import logging

import Level
import Snake

n
def create(menu, level, snake, food, win, state, name, difficulty, score):
    return {
        'menu': menu,
        'level': level,
        'snake': snake,
        'food': food,
        'win': win,
        'state': state,
        'name': name,
        'difficulty': difficulty,
        'score': score}


def show(game):
    win = getWin(game)
    food = getFood(game)
    level = getLevel(game)
    snake = getSnake(game)
    score = getScore(game)
    win.erase()
    Level.show(level, win)
    Snake.show(snake, win)
    showFood(food, win)
    showScore(score, win)
    return


def interact(game):
    snake = getSnake(game)
    food = getFood(game)
    win = getWin(game)
    score = getScore(game)
    key = win.getch()
    difficulty = game['difficulty']
    win.timeout(200-30*difficulty)
    try:
        logging.info(str(key))
        newSnake = Snake.computeNextPos(key, snake, food, win)
        game = setSnake(newSnake, game)
    except ValueError:
        logging.warning("you fail !")
        key = -1
        game = setSnake(Snake.reset(), game)
        game = setScore(0, game)
        game = setState('menu', game)

    if foodEaten(snake, food):
        game = setScore(score + 1, game)
        game = setNewFood(game)
    return


def quitGame(status, game):
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


def showFood(food, win):
    win.addstr(food[1], food[0], 'X')


def getFood(game):
    return game['food']


def setNewFood(game):
    level = getLevel(game)
    win = getWin(game)
    logging.info('food : ' + str(game['food']))
    newFoodX = random.randint(1, Level.getWidth(level))
    newFoodY = random.randint(1, Level.getHeight(level))
    while win.inch(newFoodY, newFoodY) != ord(' '):
        logging.warning('food not allowed in tha place')
        newFoodX = random.randint(1, Level.getWidth(level))
        newFoodY = random.randint(1, Level.getHeight(level))
    game['food'] = [newFoodX, newFoodY]
    logging.info('new food coords : ' + str([newFoodX, newFoodY]))
    return game


def foodEaten(snake, food):
    if food[0] == Snake.getHeadX(snake) and food[1] == Snake.getHeadY(snake):
        logging.info('some food has been eaten')
        return True
    else:
        return False


def getState(game):
    # retourne l'etat du game
    return game['state']


def setState(state, game):
    game['state'] = state
    logging.info('state set to : ' + state)
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
    logging.info('Name set to : ' + name)
    return game


def askName(game):
    # demande a l'utilisateur le nom du joueur
    win = game['win']
    win.nodelay(0)
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
    logging.info('difficulty set to : ' + str(difficulty))
    return game


def askDifficulty(game):
    # demande la difficulte a l'utilisateur
    win = game['win']
    win.nodelay(0)
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


def getScore(game):
    return game['score']


def setScore(score, game):
    game['score'] = score
    return game


def showScore(score, win):
    win.addstr(22, 4, str(score))
