import sqlite3

class connection_db:
    def __init__(self):
        self.connect= sqlite3.connect('file_last_vs.db')

    def sql_create_table(self):
        """function to create the db, not for the user"""
        self.connect.execute('''CREATE TABLE FILE_NAME
                 (old_name TXT PRIMARY KEY     NOT NULL,
                 new_name           TEXT    NOT NULL);''')
        print ("Table created successfully")
        self.connect.execute("INSERT INTO FILE_NAME VALUES('txt', 'py')")
        self.connect.commit()

    def sql_update(self, old, new):
        """update the values in the db"""
        cursorObj = self.connect.cursor()
        cursorObj.execute('UPDATE FILE_NAME SET old_name=(?)', (old,))
        cursorObj.execute('UPDATE FILE_NAME SET new_name=(?)', (new,))
        self.connect.commit()

    def sql_select_old_name(self):
        cursorObj = self.connect.cursor()
        old = cursorObj.execute('SELECT old_name FROM FILE_NAME')
        old = cursorObj.fetchall()[0][0]
        return old

    def sql_select_new_name(self):
        cursorObj = self.connect.cursor()
        new = cursorObj.execute('SELECT new_name FROM FILE_NAME')
        new = cursorObj.fetchall()[0][0]
        return new







