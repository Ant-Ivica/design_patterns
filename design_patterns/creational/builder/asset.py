class Asset(object):

    """
    Asset class containing four members (name, country, revenue and COGS), and setters for every member.
    """

    def __init__(self):
        self.name = None
        self.country = None
        self.revenue = None
        self.cogs = None

    def set_name(self, name):
        self.name = name

    def set_country(self, country):
        self.country = country

    def set_revenue(self, revenue):
        self.revenue = revenue

    def set_cogs(self, cogs):
        self.cogs = cogs
