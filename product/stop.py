from core.operate import Operate


class Stop(Operate):
    def run(self):
        print(exit)
        return False
