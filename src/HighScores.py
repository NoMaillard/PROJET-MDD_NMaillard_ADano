import pickle


def log(score, name):
    with open("highScores.dat", "rb") as f:
        highScores = pickle.load(f)
    entry = (score, name)
    highScores.append(entry)
    highScores.sort(reverse=True)
    highScores = highScores[:5]
    with open("pickles1.dat", "wb") as f:
        pickle.dump(highScores, f)
    return highScores


def get():
    with open("highScores.dat", "rb") as f:
        highScores = pickle.load(f)
    return highScores


def show(highScores, win):
    win.erase()
    for i in range(len(highScores)):
        win.addstr(10+i, 22, str(highScores[i][1]) + ' : ' + str(highScores[i][0]))
    win.addstr(9, 25, 'exit with E key')
    win.nodelay(0)
    key = win.getch()
    while key != ord('e'):
        key = win.getch()
    win.nodelay(1)
    return
