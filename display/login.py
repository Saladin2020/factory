from core.menu import Menu


class Login(Menu):

    def __init__(self):
        self.sel = -1

    def disp(self):
        print("xFile :")
        print("0. exit.")

    def cur_select(self):
        print("cur : {}".format(self.sel))

    def selection(self):
        self.sel = input("--: ")
        return self.sel

    def choice(self):
        return {
            "0": "Stop"
        }
