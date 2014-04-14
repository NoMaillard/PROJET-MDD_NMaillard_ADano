#!/usr/bin/python
import Game,Level,Snake

def init():
	global win
	curses.initscr()
    win = curses.newwin(20,80,0,0)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(0)
    
	global game,level,snake,mainMenu

	mainMenu = Menu.create('Change name','Change Difficulty','Select level','play')
	difficultyMenu = Menu.create('Easy','Normal','Difficult')
	game = Game.create()
	level = Level.create()
	snake = Snake.create()




def run():
	state = 'menu'
	while True:
		show(state)
		interact(state)
	return


def show(state):
	if state == 'menu':
		Menu.show(mainMenu)
		Menu.interact(mainMenu)
		if mainMenu['selectedItem'] == 1:
			Menu.show(difficultyMenu)
			Menu.interact(difficultyMenu)

	elif state == 'game':
		Game.show()
	return

def interact(state):
	global state
		if state == 'menu':
		Menu.interact()
	elif state == 'game':
		Game.interact()
	return
	

def quit(state):
	if state == 'menu':
		Menu.quit()
	elif state == 'game':
		Game.quit()
		
	return
	
#########################
init()
run()
quit()