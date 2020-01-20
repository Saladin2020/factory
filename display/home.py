from core.menu import Menu


class Home(Menu):

    def __init__(self):
        self.sel = -1

    def disp(self):
        print("xFile :")
        print("0. exit.")
        print("1. encode files.")
        print("2. Archives and compress files.")

    def cur_select(self):
        print("cur : {}".format(self.sel))

    def selection(self):
        self.sel = input("--: ")
        return self.sel

    def choice(self):
        return {
            "0": "Stop",
            "1": "Encode",
            "2": "Arc"
        }
