from abc import ABCMeta, abstractmethod


class Shoe(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_shoe_details():
        """This is the Shoe Interface"""
