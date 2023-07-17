import sqlite3
import queries as q
connection = sqlite3.connect('rpg_db.sqlite3')

cursor = connection.cursor()

# query = q.SELECT_ALL

results = cursor.execute(q.SELECT_ALL).fetchall()
# results = cursor.execute(q.SELECT_ALL).fetchall()
# results = cursor.execute(q.SELECT_ALL).fetchall()
# results = cursor.execute(q.SELECT_ALL).fetchall()


if __name__ == '__main__':
    print(results[:5])