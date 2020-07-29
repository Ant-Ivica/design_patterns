class PublicAsset(object):
    """
    PublicAsset class that contains 3 id elements and one mock processing method.
    """

    def __init__(self, id1: str = None, id2: str = None, id3: str = None):
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3

    def get_financial_details(self):
        print("Mapping cost of goods sold by id1".format(self.id1))
        print("Mapping revenue by id2".format(self.id2))
        print("Mapping value exchange rate by id3".format(self.id3))
