import curses


def init():

    # on initialise la fenetre curses
    curses.initscr()
    win = curses.newwin(30, 80, 0, 0)
    curses.noecho()
    curses.curs_set(0)
    win.nodelay(0)
    curses.curs_set(1)
    win.move(10, 10)
    return win


def openingMode(win):
    curses.curs_set(0)
    win.addstr(10, 20, "Chose opening mode :")
    win.addstr(11, 20, "Create new level")
    win.addstr(12, 20, "Load existing level")
    key = ' '
    cursor = 0
    while key != ord('\n'):
        if key == ord('z') or key == ord('s'):
            cursor = 1 - cursor
        win.addstr(11 + cursor, 18, '->')
        win.addstr(12 - cursor, 18, '  ')
        key = win.getch()

    levelNumber = -1
    curses.curs_set(1)
    if cursor == 0:
        level = loadNew()
    if cursor == 1:
        level, levelNumber = loadExisting(win)
    curses.curs_set(0)

    return level, levelNumber


def loadExisting(win):

    # recupere l'ensemble des niveaux
    fichier = open("levels.txt", 'r')
    chaine = fichier.read()
    levels = chaine.split('level\n')
    levelNumber = 0
    win.erase()
    curses.echo()
    win.nodelay(0)

    while levelNumber < 1 or levelNumber > len(levels) - 1:
        max = str(len(levels) - 1)
        win.addstr(10, 20, "Choose your level [ 1 - " + max + " ]")
        try:
            levelNumber = int(win.getstr(11, 20))
            if levelNumber < 1 or levelNumber > len(levels) - 1:
                raise ValueError()
        except ValueError:
            win.erase()
            win.addstr(12, 20, "retry !")

    levelStr = levels[levelNumber - 1]

    linesLevel = levelStr.split("\n")
    level = []

    for i in linesLevel:
        level.append(list(i))

    curses.noecho()
    return level, levelNumber


def loadNew():

    # on ouvre un niveau vide
    fichier = open("template.txt", 'r')
    chaine = fichier.read()
    linesLevel = chaine.split("\n")
    level = []

    for i in linesLevel:
        level.append(list(i))

    return level


def showLevel(win, level, trace):

    (y, x) = win.getyx()

    # Affiche chaque caractere de level
    for i in range(len(level)):
        for j in range(len(level[i])):
            win.addstr(i, j, level[i][j])
    win.addstr(23, 20, str(x) + ", " + str(y) + " ")

    if trace:
        win.addstr(23, 30, 'MODE : Write')
    else:
        win.addstr(23, 30, 'MODE : Move ')

    win.move(y, x)
    return


def action(win, level, trace, stop):
    (y, x) = win.getyx()

    key = win.getch()
    if key == ord(' '):
        trace = not(trace)
    if key == ord('\n'):
        stop = 1
    if key == ord('\x1b'):
        stop = 2

    if key == ord('q') and x > 1:
        x -= 1
    if key == ord('d') and x < 67:
        x += 1
    if key == ord('z') and y > 1:
        y -= 1
    if key == ord('s') and y < 19:
        y += 1

    win.move(y, x)

    if trace:
        if level[y][x] != ' ':
            level[y][x] = ' '
        else:
            level[y][x] = '+'
        changeAllTiles(win, level)
    return trace, stop


def changeAllTiles(win, level):
    for x in range(69):
        for y in range(21):
            if level[y][x] != ' ':

                c1, c2, c3, c4 = ' ', ' ', ' ', ' '

                if y > 0:
                    c1 = level[y - 1][x]
                if x < 68:
                    c2 = level[y][x + 1]
                if y < 20:
                    c3 = level[y + 1][x]
                if x > 0:
                    c4 = level[y][x - 1]
                if (c1 != ' ' and (c2 != ' ' or c4 != ' ')) or (c3 != ' ' and (c2 != ' ' or c4 != ' ')) or c1 + c2 + c3 + c4 == '    ':
                    char = '+'
                if (c1 != ' ' and c2 == ' ' and c4 == ' ') or (c3 != ' ' and c2 == ' ' and c4 == ' '):
                    char = '|'
                if (c2 != ' ' and c1 == ' ' and c3 == ' ') or (c4 != ' ' and c1 == ' ' and c3 == ' '):
                    char = '-'
                level[y][x] = char
    return


def saveLevel(level, levelNumber, win):
    curses.noecho()
    curses.curs_set(0)
    win.addstr(10, 20, "Do you want to save your level ?")
    win.addstr(11, 20, "Yes")
    win.addstr(12, 20, "No")
    key = ' '
    cursor = 0
    while key != ord('\n'):
        if key == ord('z') or key == ord('s'):
            cursor = 1 - cursor
        win.addstr(11 + cursor, 18, '->')
        win.addstr(12 - cursor, 18, '  ')
        key = win.getch()

    if cursor == 1:
        win.erase()
        win.addstr(12, 20, "Level not saved !")
        win.nodelay(0)
        key = win.getch()

    #   sauvegarde d'un nouveau level
    if levelNumber <= 0:
        fichier = open("levels.txt", 'a')
        m = len(level)
        n = len(level[1])

        for i in range(m - 1):
            s = ""
            for j in range(n):
                s = s + level[i][j]
            fichier.write(s + "\n")
        fichier.write("level\n")
    else:
    #       modif d'un level existant
        fichier = open("levels.txt", 'r+')
        s = ""
        m = len(level)
        n = len(level[1])
        for i in range(m - 1):
            for j in range(n):
                s = s + level[i][j]
            s = s + "\n"
        fichier.seek((levelNumber - 1) * (21 * 70 + 6))
        fichier.write(s)
        fichier.write("level\n")
    win.erase()
    win.addstr(12, 20, "Level saved at nubmer " + str(levelNumber) + " !")
    win.addstr(13, 20, "Hit ENTER to continue")
    win.nodelay(0)
    key = win.getch()
    return


def quit(win):

    # Restore la fenetre du terminal
    win.erase()
    curses.curs_set(0)
    curses.echo()
    curses.endwin()
    return


def start():

    trace = False
    win = init()
    level, levelNumber = openingMode(win)
    stop = 0
    win.move(10, 10)
    curses.curs_set(1)

    while not(stop):

        showLevel(win, level, trace)
        trace, stop = action(win, level, trace, stop)

    saveLevel(level, levelNumber, win)
    quit(win)
    return


if __name__ == "__main__":
    start()
