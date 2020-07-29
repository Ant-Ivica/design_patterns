from string import ascii_letters
from random import choice


class PrivateAsset(object):

    """
    PrivateAsset class that contains 3 id elements, one mock processing method and one utility random-string-generator
    method.
    """

    def __init__(self, id1: str = None, id2: str = None, id3: str = None):
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3

    def get_financial_details(self):
        print("Mapping id4 by id1".format(self.id1))
        id4 = self.generate_id4()
        print("Mapping cost of goods sold by id4".format(id4))
        print("Mapping revenue by id4".format(id4))
        print("Mapping value exchange rate by id3".format(self.id3))

    def generate_id4(self):
        letters = [choice(ascii_letters) for i in range(0, 6)]
        return "".join(letters)
