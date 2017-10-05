# -*- coding: utf-8 -*-
import curses


class Gui:

    screen = None
    screen_width = None
    screen_height = None

    def __init__(self):
        self.screen = curses.initscr()
        self.screen_widht = curses.LINES
        self.screen_height = curses.COLS

    def drawMainMenu(self):
        self.screen.addstr(2, 2, "New Game")
        self.screen.addstr(4, 2, "Exit")

    @staticmethod
    def clear_terminal():
        pass
