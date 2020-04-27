'''
off docs - https://docs.python.org/3/library/sqlite3.html
pep-249 - https://www.python.org/dev/peps/pep-0249/
'''

import sqlite3


conn = None
c = None


def open_db():
    global conn
    global c
    conn = sqlite3.connect('TestData/sqlite_userdb.db')
    c = conn.cursor()


def create_table():
    # Create table
    global conn
    global c
    c.execute('''CREATE TABLE users
                (ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    user text NOT NULL UNIQUE, password BLOB, dir text, enc_key BLOB)''')
    conn.commit()


def insert(user, password, user_dir, enc_key):
    global conn
    global c
    c.execute("INSERT INTO users (user, password, dir, enc_key) \
                        VALUES (?,?,?,?)", (
                                                user,
                                                password,
                                                user_dir,
                                                enc_key))
    conn.commit()


def select(user):
    global conn
    global c
    c.execute("SELECT * FROM users WHERE user=?", (user, ))
    rows = c.fetchall()
    # conn.commit()
    return rows


def update(user, password=None, user_dir=None, enc_key=None):
    global conn
    global c
    req = ""
    if password is not None:
        req += "password = '" + password + "'"
    if user_dir is not None:
        if len(req) > 0:
            req += ", "
        req += "dir = '" + user_dir + "'"
    if enc_key is not None:
        if len(req) > 0:
            req += ", "
        req += "enc_key = '" + enc_key + "'"
        
    c.execute("UPDATE users SET {0} WHERE user = '{1}'".format(req, user))
    conn.commit()


def delete(user: str):
    global conn
    global c
    c.execute("DELETE FROM users WHERE user=?", (user, ))
    conn.commit()


def close_db():
    global conn
    conn.close()


if __name__ == "__main__":
    open_db()
    # create_table()
    # delete("user3")
    # insert("user3", "5345345", "dir1", "key1")
    # insert("user4", "pas1", "dir1", "key1")
    # delete("user3")
    update('user3', 'keklol')
    print(select('user3'))
    print(select('user4'))
    close_db()
