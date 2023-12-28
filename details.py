import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT, names CHAR(15))")
conn.commit()
def AddUser(id,name):
    "add user to database"
    cursor.execute("INSERT INTO users (id,names) VALUES (?,?)", (id,name))
    conn.commit()
def GetUserName(id):
    "return user's name by id"
    cursor.execute("SELECT names FROM users WHERE id = ?", (id))
    return cursor.fetchall()[0][0]