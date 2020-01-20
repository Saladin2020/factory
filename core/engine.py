import os
from display import *
from product import *
class Engine:

    def __init__(self, display):
        state = None
        menu = eval(display)()
        while state == None:
            os.system("cls")
            menu.disp()
            menu.cur_select()
            state = self.__build(menu.selection(), menu.choice())

    def __build(self, select_position, p):
        if select_position in p.keys():
            return eval(p[select_position])().run()
