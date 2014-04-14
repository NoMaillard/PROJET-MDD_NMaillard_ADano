#!/usr/bin/python
import curses
from curses import KEY_UP, KEY_DOWN

import Settings

curses.initscr()
win = curses.newwin(20,80,0,0)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(0)


def launch():
	global settings
	name = "Player1"
	difficulty = 2
	levelNumber = 1
	menuItem = ["levelNumber","playerName","difficulty","HighScores","Start"]
	settings = {'playerName' : name, 'difficulty' : difficulty, 'levelNumber' : levelNumber}
	menuCursor = 0
	show(menuCursor)
	key = 0
	win.clear()
	while key != 27:
		win.border(0)

		show(menuCursor)
		key = win.getch()
		
		if key  == ord('z'):
			if menuCursor != 0:
				menuCursor -= 1
		if key == ord('s'):
			if menuCursor != len(menuItem)-1:
				menuCursor += 1
		if key == ord('e'):
			if menuCursor < 3:
				itemSetting,itemVariable = Settings.askSetting(menuItem[menuCursor])
				settings[itemSetting] = itemVariable
			elif menuCursor == 3:
				HighScores.show()
			elif menuCursor == 4:
				curses.nocbreak()
				curses.echo()
				curses.endwin()
				return settings
	
		win.erase()

def show(menuCursor):
	if menuCursor == 0:
		win.addstr(10,20,"->Choisir le niveau    ")
	else:
		win.addstr(10,22,"Choisir le niveau    ")
	if menuCursor == 1:
		win.addstr(11,20,"->Choisir le nom    ")
	else:
		win.addstr(11,22,"Choisir le nom    ")
	if menuCursor == 2:
		win.addstr(12,20,"->Choisir la difficulte    ")
	else:
		win.addstr(12,22,"Choisir la difficulte    ")
	if menuCursor == 3:
		win.addstr(13,20,"->Afficher les meilleurs scores    ")
	else:
		win.addstr(13,22,"Afficher les meilleurs scores     ")
	if menuCursor == 4:
		win.addstr(14,20,"->Demarrer le niveau     ")
	else:
		win.addstr(14,22,"Demarrer le niveau     ")
	win.addstr(2,3,settings['playerName'])
	win.addstr(3,3,"Niveau : "+str(settings['levelNumber']))
	win.addstr(4,3,"Difficulte : "+str(settings['difficulty']))




if __name__ == '__main__':
	launch()
