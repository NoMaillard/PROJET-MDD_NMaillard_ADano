#!/usr/bin/python
import curses


def create(*argv):
    menuCursor = 0
    selectedItem = -1
    menuItems = []
    j = 0
    for i in argv:
        menuItems.append(i)
        j += 1
    menu = {'items' : menuItems,'cursor' : menuCursor,'selectedItem' : selectedItem}
    return menu

def show(menu):
    global win
    win.erase()
    for i in range(len(menu['items'])): 
        if i == menu['cursor']:
            win.addstr(10+i,20,"->"+str(menu['items'][i]))
        else:
            win.addstr(10+i,22,str(menu['items'][i]))
    return

def interact(menu):
    global win
    menu['selectedItem'] = -1

    key = win.getch()
    if key == ord('z'):
        if menu['cursor'] != 0:
            menu['cursor'] -= 1
    if key == ord('s'):
        if menu['cursor'] != len(menu['items'])-1:
            menu['cursor'] += 1
    if key == ord('e'):
        menu['selectedItem'] = menu['cursor']
    return menu

def quit():
    global state
    state = 'game'
    return


if __name__ == '__main__':
    global win
    curses.initscr()
    win = curses.newwin(20,80,0,0)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(0)
    menu = create('First','second','third')
    submenu = create('zelfjez','zaefef')
    while True:
        show(menu)
        interact(menu)
        if menu['selectedItem'] == 0:
            while True:
                show(submenu)
                interact(submenu)
                if submenu['selectedItem'] == 1:
                    break
