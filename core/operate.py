from abc import ABCMeta, abstractmethod

class Operate(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        raise NotImplementedError('Not Implemented Error')