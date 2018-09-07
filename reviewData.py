import os
import fnmatch
import fileinput
import xml.etree.ElementTree as ET
import sqlite3
from dateutil import parser
from datetime import datetime as dt

def exploreFile():
    conn = sqlite3.connect('matches.db')
    c = conn.cursor()
    c.execute('SELECT * FROM match LIMIT 3 offset 1300')

    someGames = c.fetchall()
    for game in someGames:
        print('---------------')
        print(game[39])
        print(game[40])
        print(game[41])
        print('---------------')
    conn.close()

if __name__ == "__main__":
    exploreFile()