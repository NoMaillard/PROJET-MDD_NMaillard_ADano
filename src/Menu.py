import curses
from curses import KEY_UP, KEY_DOWN

import Settings

curses.initscr()
win = curses.newwin(30,70,0,0)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(0)


def launch():
	menuItem = ["levelNumber","playerName","difficulty"]
	menuCursor = 0
	show(menuCursor)
	key = 0
	while key != 27:
		win.border(0)
		key = win.getch()
		if key  == ord('z'):
			if menuCursor != 0:
				menuCursor -= 1
		if key == ord('s'):
			if menuCursor != len(menuItem)-1:
				menuCursor += 1
		if key == ord('e'):
			Settings.askSetting(menuItem[menuCursor])
		win.refresh()
		show(menuCursor)

def show(menuCursor):
	if menuCursor == 0:
		win.addstr(10,20,"[Choisir le nievau]    ")
	else:
		win.addstr(10,20,"Choisir le nievau    ")
	if menuCursor == 1:
		win.addstr(11,20,"[Choisir le nom]    ")
	else:
		win.addstr(11,20,"Choisir le nom    ")
	if menuCursor == 2:
		win.addstr(12,20,"[Choisir la difficulte]    ")
	else:
		win.addstr(12,20,"Choisir la difficulte    ")



if __name__ == '__main__':
	launch()
