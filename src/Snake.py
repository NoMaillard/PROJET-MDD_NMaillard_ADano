# import logging


def create(headXPos, headYPos, headFacing, length):
    snakeBody = []
    for i in range(length):
        snakeBody.append([])
        if headFacing == 0:     # 0 : haut
            snakeBody[i].append(headXPos)
            snakeBody[i].append(headYPos + i)
        if headFacing == 1:     # 1 : droite
            snakeBody[i].append(headXPos - i)
            snakeBody[i].append(headYPos)
        if headFacing == 2:     # 2 : bas
            snakeBody[i].append(headXPos)
            snakeBody[i].append(headYPos - i)
        if headFacing == 3:     # 3 : gauche
            snakeBody[i].append(headXPos + i)
            snakeBody[i].append(headYPos)
    snake = {'snakeBody': snakeBody,
             'headFacing': headFacing,
             'length': length}
    return snake


def show(snake, win):
    snakeBody = snake['snakeBody']
    for i in range(len(snakeBody)):
        win.addstr(snakeBody[i][1], snakeBody[i][0], 'O')


def computeNextPos(key, snake, food, win):
    snakeBody = snake['snakeBody']
    headFacing = snake['headFacing']
    if key == ord('z') and not headFacing == 2:
        headFacing = 0
    elif key == ord('d') and not headFacing == 3:
        headFacing = 1
    elif key == ord('s') and not headFacing == 0:
        headFacing = 2
    elif key == ord('q') and not headFacing == 1:
        headFacing = 3

    if headFacing == 0:
        newHeadX = snakeBody[0][0]
        newHeadY = snakeBody[0][1] - 1
    elif headFacing == 1:
        newHeadX = snakeBody[0][0] + 1
        newHeadY = snakeBody[0][1]
    elif headFacing == 2:
        newHeadX = snakeBody[0][0]
        newHeadY = snakeBody[0][1] + 1
    elif headFacing == 3:
        newHeadX = snakeBody[0][0] - 1
        newHeadY = snakeBody[0][1]

    newHeadplace = win.inch(newHeadY, newHeadX)
    if newHeadplace != ord(' ') and newHeadplace != ord('X'):
        raise ValueError()

    snakeBody.insert(0, [newHeadX, newHeadY])
    if not food == snakeBody[0]:
        snakeBody.pop()
    snake['headFacing'] = headFacing
    snake['snakeBody'] = snakeBody
    return snake


def getHeadX(snake):
    snakeBody = snake['snakeBody']
    return snakeBody[0][0]


def getHeadY(snake):
    snakeBody = snake['snakeBody']
    return snakeBody[0][1]


def reset():
    return create(35, 15, 1, 2)
