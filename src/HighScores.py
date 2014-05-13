import pickle


def write(score, name):

    try:
        with open("highScores.dat", "rb") as f:
            highScores = pickle.load(f)
    except EOFError:
        highScores = []

    entry = (score, name)
    highScores.append(entry)
    highScores.sort(reverse=True)
    highScores = highScores[:5]

    with open("pickles1.dat", "wb") as f:
        pickle.dump(highScores, f)

    return highScores
