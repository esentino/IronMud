# -*- coding: utf-8 -*-
from ironmud.gui import Gui
import curses

class TestGui:

    def test_screen_size(self):
        g = Gui()
        assert g.screen_height is not None
        assert g.screen_widht is not None

    def test_draw_main_menu(self):
        g = Gui()
        g.drawMainMenu()
        assert g.screen.inch(2, 2) == ord('N')
        assert g.screen.inch(4, 2) == ord('E')
        assert g.screen.inch(2, 3) == ord('e')