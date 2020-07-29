from design_patterns.creational.singleton.connection import Connection


class DataBase(object):

    """
    Database class written in a singleton form.
    """

    # initialize the variable that will store the single object instance
    _instance = None

    def __new__(self):
        """
        __new__ is a predefined class function that is called before the constructor function (__init__). Here, on first
        instantiation of the DataBase class, it will create and store itself in the variable initialized above. Every
        time the application tries to instantiate a new object, it will return the same one instead.
        """
        if self._instance is None:
            self._instance = super(DataBase, self).__new__(self)
        return self._instance

    def build(self):
        """
        After the object has been instantiated, we need to run a function that will construct the class members, and in
        this case, that means setting up database connection(s). We're using a mock class for this.
        """
        self.connection = Connection()

    def get_db_session(self):
        """
        Returns a mock session created by Connection class instance.
        """
        return self.connection.get_session()
