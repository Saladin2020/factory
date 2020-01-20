from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):

    @abstractmethod
    def disp(self):
        raise NotImplementedError('Not Implemented Error')

    @abstractmethod
    def cur_select(self):
        raise NotImplementedError('Not Implemented Error')

    @abstractmethod
    def selection(self):
        raise NotImplementedError('Not Implemented Error')

    @abstractmethod
    def choice(self):
        raise NotImplementedError('Not Implemented Error')
