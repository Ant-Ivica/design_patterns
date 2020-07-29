class Connection(object):

    """
    Simple Connection class that will be used in tandem with DataBase Singleton class. This serves as a mock class for
    database session factory. On initialization, prints a statement that connection was successfully established.
    Method get_session returns a mocked connection session in a form of a string.
    """

    def __init__(self):
        print("Connection established")

    def get_session(self):
        return "ExampleDB Connection"
