import pickle
import curses


def log(score, name, difficuty):
    if difficuty == 1:
        difficuty = 'Easy'
    if difficuty == 2:
        difficuty = 'Medium'
    if difficuty == 3:
        difficuty = 'Hard'
    try:
        with open("highScores"+difficuty+".dat", "rb") as f:
            highScores = pickle.load(f)
    except EOFError:
        highScores = []
    entry = (score, name)
    highScores.append(entry)
    highScores.sort(reverse=True)
    highScores = highScores[:5]
    with open("highScores"+difficuty+".dat", "wb") as f:
        pickle.dump(highScores, f)
    return highScores


def get():
    highScores = []
    try:
        with open("highScoresEasy.dat", "rb") as f:
            highScores.append(pickle.load(f))
    except EOFError:
        highScores.append([])
    try:
        with open("highScoresMedium.dat", "rb") as f:
            highScores.append(pickle.load(f))
    except EOFError:
        highScores.append([])
    try:
        with open("highScoresHard.dat", "rb") as f:
            highScores.append(pickle.load(f))
    except EOFError:
        highScores.append([])

    return highScores


def show(highScores, win):
    win.erase()
    column = 10
    for table in highScores:
        for i in range(len(table)):
            win.addstr(10+i, column, str(table[i][1]) + ' : ' + str(table[i][0]))
        column += 15
    win.addstr(9, 10, 'Easy', curses.color_pair(1))
    win.addstr(9, 25, 'Medium', curses.color_pair(2))
    win.addstr(9, 40, 'Hard', curses.color_pair(3))
    win.addstr(5, 25, 'HIGHSCORES')
    win.addstr(17, 24, 'Quit with ENTER')
    win.nodelay(0)
    key = win.getch()
    while key != ord('\n'):
        key = win.getch()
    win.nodelay(1)
    return
