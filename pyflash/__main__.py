import os
import sys

import curses
import subprocess

GAMES_DIR = '/home/picles/PyFlash/games'

GAMES = os.listdir(GAMES_DIR)
GAMES.append('Exit')

def menu(stdscr):
    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0
    option = 0
    while c != 10:
        stdscr.erase()
        stdscr.addstr("=== PyFlash ===\n", curses.A_UNDERLINE)
        stdscr.addstr("Select your game\n\n", curses.A_UNDERLINE)
        for i in range(len(GAMES)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}. ".format(i + 1))
            stdscr.addstr(GAMES[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(GAMES) - 1:
            option += 1

    game = GAMES[option]
    
    if (game == "Exit"):
      exit()
    
    stdscr.addstr("Playing {0}".format(game))
    return game    

while True:
  game = curses.wrapper(menu)
  print('\nRunning {} in PyFlash\nHave Fun! :D'.format(game))
  subprocess.call("./pyflash/flashrunner/flashplayer {}".format(GAMES_DIR + '/' + game), cwd=os.getcwd(), shell=True, stdout=subprocess.PIPE)