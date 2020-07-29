from abc import ABCMeta, abstractmethod


class BaseShoeFactory(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_shoe(self):
        """This is the Base Shoe Factory Interface"""
