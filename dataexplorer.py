import os
import fnmatch
import fileinput
import xml.etree.ElementTree as ET
import sqlite3
from dateutil import parser

class matchCls():
  def __init__(self, matchDate, matchId, teamOneName, teamOneId, teamTwoName, teamTwoId, teamOneGoals, teamTwoGoals, location, season):
    self.matchDate = matchDate
    self.teamOneName = teamOneName
    self.teamOneId = teamOneId
    self.teamTwoName = teamTwoName
    self.teamTwoId = teamTwoId
    self.teamOneGoals = teamOneGoals
    self.teamTwoGoals = teamTwoGoals
    self.matchId = matchId
    self.location = location
    self.wind = '12'
    self.percip = 'None'
    self.temp = '0'
    self.season = season
    self.teamOneResult = self.teamOneResult()
    self.teamTwoResult = self.teamTwoResult()
    self.query = self.createSQLQuery()

  def teamOneResult(self):
    #2 = win, 1 = tie, 0 = loss
    if int(self.teamOneGoals) > int(self.teamTwoGoals):
      teamOneResult = '2' 
    elif int(self.teamOneGoals) == int(self.teamTwoGoals):
      teamOneResult = '1'
    elif int(self.teamOneGoals) < int(self.teamTwoGoals):
      teamOneResult = '0'

    return teamOneResult

  def teamTwoResult(self):
    if int(self.teamOneGoals) > int(self.teamTwoGoals):
      teamTwoResult = '0' 
    elif int(self.teamOneGoals) == int(self.teamTwoGoals):
      teamTwoResult = '1'
    elif int(self.teamOneGoals) < int(self.teamTwoGoals):
      teamTwoResult = '2'

    return teamTwoResult

  def createSQLQuery(self):
    #id INTEGER PRIMARY KEY AUTOINCREMENT, 
    #season YEAR, 
    #date DATETIME, 
    #team1 TINYINT, 
    #team2 TINYINT, 
    #wind TINYINT, 
    #percip TINYTEXT, 
    #temp TINYINT, 
    #team1Result TINYINT, 
    #team2Result TINYINT, 
    #team1Goals TINYINT, 
    #team2Goals TINYINT
    query = 'INSERT INTO match VALUES'
    query += '('+self.matchId+','
    query += '"'+self.season+'",'
    query += '"'+self.matchDate.strftime('%Y-%m-%d')+'",'
    query += self.teamOneId+','
    query += self.teamTwoId+','
    query += self.wind+','
    query += '"'+self.percip+'",'
    query += self.temp+','
    query += self.teamOneResult+','
    query += self.teamTwoResult+','
    query += self.teamOneGoals+','
    query += self.teamTwoGoals+')'
    return query

def exploreFile():
  files = ['2013', '2014', '2015', '2016', '2017']
  conn = sqlite3.connect('matches.db')
  c = conn.cursor()
  createTables(conn,c)
  numberOfGames = 0
  for year in files:
    tree = ET.parse('data/'+year+'.xml')
    root = tree.getroot()
    for match in root:
      if match[9].text != 'false': 
        matchDate = parser.parse(match[6].text)
        teamOneName = match[12][3].text
        teamOneId = match[12][2].text
        teamTwoName = match[13][3].text
        teamTwoId = match[13][2].text
        matchId = match[8].text
        teamOneGoals = match[10][1][0].text
        teamTwoGoals = match[10][1][1].text
        if match[5].attrib:
          location = ''
        else:
          location = match[5][1].text

        numberOfGames += 1

        matchObj = matchCls(matchDate, matchId, teamOneName, teamOneId, teamTwoName, teamTwoId, teamOneGoals, teamTwoGoals, location, year)
        checkIfTeamsExist(teamOneName, teamOneId, teamTwoName, teamTwoId, c)
        insertMatch(matchObj,c)

  print('Number of games ' + str(numberOfGames))


def insertMatch(match, cursor):
  cursor.execute(match.query)

def checkIfTeamsExist(teamOneName, teamOneId, teamTwoName, teamTwoId, cursor):
  teams = cursor.execute('''SELECT * FROM team''')
  teamOneExists = False
  teamTwoExists = False

  for team in teams:
    if str(team[0]) == teamOneId:
      teamOneExists = True

    if str(team[0]) == teamTwoId:
      teamTwoExists = True
  
  if not teamOneExists:
    teamToInsert = [(teamOneId,teamOneName)]
    cursor.executemany('INSERT INTO team VALUES (?,?)', teamToInsert)
  if not teamTwoExists:
    teamToInsert = [(teamTwoId,teamTwoName)]
    cursor.executemany('INSERT INTO team VALUES (?,?)', teamToInsert)

def createTables(conn, cursor):
  cursor.execute('''CREATE TABLE IF NOT EXISTS match (id INTEGER PRIMARY KEY AUTOINCREMENT, season YEAR, date DATETIME, team1 TINYINT, team2 TINYINT, wind TINYINT, percip TINYTEXT, temp TINYINT, team1Result TINYINT, team2Result TINYINT, team1Goals TINYINT, team2Goals TINYINT)''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS team (id INTEGER PRIMARY KEY AUTOINCREMENT, name TINYTEXT)''')

if __name__ == "__main__":
    exploreFile()
