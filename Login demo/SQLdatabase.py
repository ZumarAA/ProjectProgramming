# create three tables
import sqlite3


# this module has SQL code to create tables, add users' account details, and search for a user
def create_database():  # creates the table
    conn = sqlite3.connect("usersAccount.db")
    cursor = conn.cursor()
    # Create a table to store user credentials
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT,
                       password TEXT)''')
    conn.close()

 # the function below seraches for a user in the table
def searchUser(givenUser, givenpassword):
    conn = sqlite3.connect('usersAccount.db')
    # Select all records in a table:
    cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
    for row in cursor:

        if row[0] == givenUser and row[1] == givenpassword:

            return True

    return False

# the function below used to add some user accounts (for testing only)
def adduser(user, hashpass):
    create_database()
    # Add a sample user for testing
    conn = sqlite3.connect("usersAccount.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
                   (user, hashpass))

    conn.commit()



# select data from the tables
if __name__ == "__main__":
    # test data
    # username = "abid"
    # password = "password321"
    # import process
    # password = process.hash_input(password)
    # adduser(username, password)
    pass