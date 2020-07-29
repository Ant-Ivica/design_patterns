from design_patterns.creational.singleton.database import DataBase

# initialize DataBase object for the first time and 'build' it.
db = DataBase()
db.build()

# try to create new instances of DataBase objects
db_1 = DataBase()
db_2 = DataBase()

# prints to show that the two new instances are actually the same (same memory reference as well)
print(db_1 == db_2)
print(db_1, db_2)

# get sessions from each 'new' db instance
session_1 = db_1.get_db_session()
session_2 = db_2.get_db_session()

# prints to show that the 'new' db instances are using the connection built in the first instance
print(session_1 == session_2)
