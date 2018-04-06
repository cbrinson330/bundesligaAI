import os
import fnmatch
import fileinput
import xml.etree.ElementTree as ET
import sqlite3
from dateutil import parser

class matchCls():
  def __init__(self, matchDate, matchId, teamOneName, teamTwoName, teamOneGoals, teamTwoGoals, location):
    self.matchDate = matchDate
    self.teamOneName = teamOneName
    self.teamTwoName = teamTwoName
    self.teamOneGoals = teamOneGoals
    self.teamTwoGoals = teamTwoGoals
    self.matchId = matchId
    self.location = location
    self.teamOneResult = self.teamOneResult()
    self.teamTwoResult = self.teamTwoResult()

  def teamOneResult(self):
    #2 = win, 1 = tie, 0 = loss
    if int(self.teamOneGoals) > int(self.teamTwoGoals):
      teamOneResult = 2 
    elif int(self.teamOneGoals) == int(self.teamTwoGoals):
      teamOneResult = 1
    elif int(self.teamOneGoals) < int(self.teamTwoGoals):
      teamOneResult = 0 

    return teamOneResult

  def teamTwoResult(self):
    if int(self.teamOneGoals) > int(self.teamTwoGoals):
      teamTwoResult = 0 
    elif int(self.teamOneGoals) == int(self.teamTwoGoals):
      teamTwoResult = 1
    elif int(self.teamOneGoals) < int(self.teamTwoGoals):
      teamTwoResult = 2 

    return teamTwoResult

def exploreFile():
  #fileName = 'data/2015';
  tree = ET.parse('data/2015.xml')
  root = tree.getroot()
  for match in root:
    print(match)
    matchDate = parser.parse(match[6].text)
    teamOneName = match[12][0].text
    teamTwoName = match[13][0].text
    matchId = match[8].text
    teamOneGoals = match[10][1][0].text
    teamTwoGoals = match[10][1][1].text
    if match[5].attrib:
      location = ''
    else:
      location = match[5][1].text

    matchObj = matchCls(matchDate, matchId, teamOneName, teamTwoName, teamOneGoals, teamTwoGoals, location)

    conn = sqlite3.connect('matches.db')
    c = conn.cursor()
    createTables(conn,c)
    checkIfTeamsExist(teamOneName, teamTwoName, c)
    insertMatch(matchObj,c)


def insertMatch(match, c):
  cursor.execute('INSERT INTO match VALUES ("'+match.teamOneName+'")')
  #id INTEGER PRIMARY KEY AUTOINCREMENT, 
  #season YEAR, 
  #date DATETIME, 
  #team1 TINYINT, 
  #team2 TINYINT, 
  #wind TINYINT, 
  #percip TINYTEXT, 
  #team1Goals TINYINT, 
  #team2Goals TINYINT

def checkIfTeamsExist(teamOneName, teamTwoName, cursor):
  teams = cursor.execute('''SELECT name FROM teams''')
  teamOneExists = False
  teamTwoExists = False

  for team in teams:
    if team == teamOneName:
      teamOneExists = True

    if team == teamTwoName:
      teamTwoExists = True
  
  if not teamOneExists:
    cursor.execute('INSERT INTO team VALUES (0,"'+teamOneName+'")')
  if not teamTwoExists:
    cursor.execute('INSERT INTO team VALUES (0,"'+teamTwoName+'")')


def createTables(conn, cursor):
  cursor.execute('''CREATE TABLE IF NOT EXISTS match (id INTEGER PRIMARY KEY AUTOINCREMENT, season YEAR, date DATETIME, team1 TINYINT, team2 TINYINT, wind TINYINT, percip TINYTEXT, team1Goals TINYINT, team2Goals TINYINT)''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS team (id INTEGER PRIMARY KEY AUTOINCREMENT, name TINYTEXT)''')

if __name__ == "__main__":
    exploreFile()