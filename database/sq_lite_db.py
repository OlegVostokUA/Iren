import sqlite3 as sq
from datetime import datetime


def sql_start():
    # create  table
    global base, cur
    base = sq.connect('iren_database.db')
    cur = base.cursor()
    if base:
        print('Data base admin connection=Done')
    base.execute('CREATE TABLE IF NOT EXISTS rating_food('
                 'date TEXT, '
                 'division TEXT, '
                 'food_intake TEXT, '
                 'mark INT, '
                 'identif TEXT)')


def add_to_db(data):
    cur.execute("""INSERT INTO rating_food VALUES (?, ?, ?, ?, ?)""", data)
    base.commit()


def read_db(div_intake):
    data_in = (datetime.today().strftime("%d.%m.%Y"),) + (div_intake,)
    data = cur.execute("""SELECT * FROM rating_food WHERE date == ? AND division == ?""", data_in).fetchall()
    return data


def select_marks():
    dates = (datetime.now().replace(day=1).strftime('%d.%m.%Y'), datetime.now().strftime('%d.%m.%Y'))
    # data = cur.execute("""SELECT date, mark FROM rating_food""").fetchall()
    data = cur.execute("""SELECT date, division, mark FROM rating_food WHERE date BETWEEN ? AND ?""", dates).fetchall()
    return data
