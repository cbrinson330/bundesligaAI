import os
import fnmatch
import fileinput
import xml.etree.ElementTree as ET
import sqlite3
from dateutil import parser
from datetime import datetime as dt

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
    self.wind = '0'
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
    query += self.teamTwoGoals+','
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0,'
    query += '0)'
    return query

def exploreFile():
  files = ['2013', '2014', '2015', '2016', '2017', '2018']
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
  populateHistoricalValues(c)
  reviewData(c)
  conn.commit()
  conn.close()

def insertMatch(match, cursor):
  cursor.execute(match.query)
  #Get previous games this season

def populateHistoricalValues(cursor):
  cursor.execute('''SELECT * FROM team''')
  allTeams = cursor.fetchall()
  printTeamInfo = True
  for team in allTeams:
    teamId = str(team[0])
    cursor.execute('SELECT * FROM match WHERE team1 = ' + teamId + ' OR team2 =' + teamId)
    allGamesForTeam = cursor.fetchall()
    for gameData in allGamesForTeam:
      if gameData[3] == teamId:
        isHomeTeam = True
        opponent = gameData[4]
      else:
        isHomeTeam = False
        opponent = gameData[3]

      year = gameData[1]
      date = dt.strptime(gameData[2], "%Y-%m-%d")
      # date = gameData[2]
      lifetimeWins = 0
      lifetimeLoss = 0
      lifetimeTie = 0
      seasonWins = 0
      seasonTie = 0
      seasonLoss = 0
      seasonOpponentWins = 0
      seasonOpponentTies = 0
      seasonOpponentLoss = 0
      lifetimeGoalsScoredOpponent = 0
      lifetimeGoalsAllowedOpponent = 0
      goalsAllowedThisSeason = 0
      goalsScoredThisSeason = 0
      goalsScoredThisSeasonOpponent = 0
      goalsAllowedThisSeasonOpponent = 0
      
      for gameDataB in allGamesForTeam:

        gameBDate = dt.strptime(gameDataB[2], "%Y-%m-%d")

        #Don't count same game
        if gameData[0] != gameDataB[0]:

          #check if is same season
          if year == gameDataB[1]:
            if gameBDate < date:
              if int(teamId) == int(gameDataB[3]):
                # Is Home game
                seasonGameResult = gameDataB[8]
                goalsAllowedThisSeason += gameDataB[10]
                goalsScoredThisSeason += gameDataB[11]

              if int(teamId) == int(gameDataB[4]):
                #Is Away Game
                seasonGameResult = gameDataB[9]
                goalsAllowedThisSeason += gameDataB[11]
                goalsScoredThisSeason += gameDataB[10]

              #2 = win, 1 = tie, 0 = loss
              if seasonGameResult == 2:
                seasonWins += 1
              elif seasonGameResult == 1:
                seasonTie += 1
              elif seasonGameResult == 0:
                seasonLoss += 1

              res = None
              # Get current season reccord against current opponent
              if int(gameDataB[4]) == int(teamId):
                #is Away Game
                res = gameDataB[9]
                goalsAllowedThisSeasonOpponent += int(gameDataB[11])
                goalsScoredThisSeasonOpponent += int(gameDataB[10])

              elif int(gameDataB[3]) == int(teamId):
                #is Home Game
                res = gameDataB[8]
                goalsAllowedThisSeasonOpponent += int(gameDataB[10])
                goalsScoredThisSeasonOpponent += int(gameDataB[11])
              
              #2 = win, 1 = tie, 0 = loss
              if res == 2:
                seasonOpponentWins += 1
              elif res == 1:
                seasonOpponentTies += 1
              elif res == 0:
                seasonOpponentLoss += 1

          #check if is any season against the same opponent
          result = None
          if gameBDate < date:
            if int(gameDataB[4]) == int(teamId):
              # is away game
              result = gameDataB[9]
              lifetimeGoalsAllowedOpponent += int(gameDataB[11])
              lifetimeGoalsScoredOpponent += int(gameDataB[10])

            elif int(gameDataB[3]) == int(teamId):
              #is home game
              result = gameData[8]
              lifetimeGoalsAllowedOpponent += int(gameDataB[10])
              lifetimeGoalsScoredOpponent += int(gameDataB[11])

            #2 = win, 1 = tie, 0 = loss
            if result == 2:
              lifetimeWins += 1
            elif result == 1:
              lifetimeTie += 1
            elif result == 0:
              lifetimeLoss += 1

      if int(gameData[3]) == int(teamId):
        cursor.execute('''UPDATE match SET 
                                      team1GoalsScoredThisSeason = ?,
                                      team1GoalsAllowedThisSeason = ?,
                                      team1GoalsScoredThisSeasonOpponent = ?,
                                      team1GoalsAllowedThisSeasonOpponent = ?,
                                      team1LifetimeGoalsScoredOpponent = ?,
                                      team1LifetimeGoalsAllowedOpponent = ?,
                                      team1SeasonWins = ?,
                                      team1SeasonTie = ?,
                                      team1SeasonLoss = ?,
                                      team1SeasonOppWins = ?,
                                      team1SeasonOppTie = ?,
                                      team1SeasonOppLoss = ?,
                                      team1LifetimeOppWins = ?,
                                      team1LifetimeOppTie = ?,
                                      team1LifetimeOppLoss = ?
                                  WHERE id = ?''',
                                  (goalsScoredThisSeason,
                                  goalsAllowedThisSeason,
                                  goalsScoredThisSeasonOpponent,
                                  goalsAllowedThisSeasonOpponent,
                                  lifetimeGoalsScoredOpponent,
                                  lifetimeGoalsAllowedOpponent,
                                  seasonWins,
                                  seasonTie,
                                  seasonLoss,
                                  seasonOpponentWins,
                                  seasonOpponentTies,
                                  seasonOpponentLoss,
                                  lifetimeWins,
                                  lifetimeTie,
                                  lifetimeLoss,
                                  gameData[0]))
      elif int(gameData[4]) == int(teamId):
        cursor.execute('''UPDATE match SET 
                                      team2GoalsScoredThisSeason = ?,
                                      team2GoalsAllowedThisSeason = ?,
                                      team2GoalsScoredThisSeasonOpponent = ?,
                                      team2GoalsAllowedThisSeasonOpponent = ?,
                                      team2LifetimeGoalsScoredOpponent = ?,
                                      team2LifetimeGoalsAllowedOpponent = ?,
                                      team2SeasonWins = ?,
                                      team2SeasonTie = ?,
                                      team2SeasonLoss = ?,
                                      team2SeasonOppWins = ?,
                                      team2SeasonOppTie = ?,
                                      team2SeasonOppLoss = ?,
                                      team2LifetimeOppWins = ?,
                                      team2LifetimeOppTie = ?,
                                      team2LifetimeOppLoss = ?
                                  WHERE id = ?''',
                                  (goalsScoredThisSeason,
                                  goalsAllowedThisSeason,
                                  goalsScoredThisSeasonOpponent,
                                  goalsAllowedThisSeasonOpponent,
                                  lifetimeGoalsScoredOpponent,
                                  lifetimeGoalsAllowedOpponent,
                                  seasonWins,
                                  seasonTie,
                                  seasonLoss,
                                  seasonOpponentWins,
                                  seasonOpponentTies,
                                  seasonOpponentLoss,
                                  lifetimeWins,
                                  lifetimeTie,
                                  lifetimeLoss,
                                  gameData[0]))

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
    teamToInsert = [(int(teamOneId),teamOneName)]
    cursor.executemany('INSERT INTO team VALUES (?,?)', teamToInsert)
  if not teamTwoExists:
    teamToInsert = [(int(teamTwoId),teamTwoName)]
    cursor.executemany('INSERT INTO team VALUES (?,?)', teamToInsert)

def reviewData(cursor):
  cursor.execute('SELECT * FROM match LIMIT 10 offset 1448')

  someGames = cursor.fetchall()
  for game in someGames:
    print(game)

def createTables(conn, cursor):
  cursor.execute('''CREATE TABLE IF NOT EXISTS match (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                      season YEAR, 
                                                      date DATETIME, 
                                                      team1 TINYINT, 
                                                      team2 TINYINT, 
                                                      wind TINYINT, 
                                                      percip TINYTEXT, 
                                                      temp TINYINT, 
                                                      team1Result TINYINT, 
                                                      team2Result TINYINT, 
                                                      team1Goals TINYINT, 
                                                      team2Goals TINYINT,
                                                      team1GoalsScoredThisSeason TINYINT,
                                                      team2GoalsScoredThisSeason TINYINT,
                                                      team1GoalsAllowedThisSeason TINYINT,
                                                      team2GoalsAllowedThisSeason TINYINT,
                                                      team1GoalsScoredThisSeasonOpponent TINYINT,
                                                      team2GoalsScoredThisSeasonOpponent TINYINT,
                                                      team1GoalsAllowedThisSeasonOpponent TINYINT,
                                                      team2GoalsAllowedThisSeasonOpponent TINYINT,
                                                      team1LifetimeGoalsScoredOpponent TINYINT,
                                                      team2LifetimeGoalsScoredOpponent TINYINT,
                                                      team1LifetimeGoalsAllowedOpponent TINYINT,
                                                      team2LifetimeGoalsAllowedOpponent TINYINT,
                                                      team1SeasonWins TINYINT,
                                                      team2SeasonWins TINYINT,
                                                      team1SeasonLoss TINYINT,
                                                      team2SeasonLoss TINYINT,
                                                      team1SeasonTie TINYINT,
                                                      team2SeasonTie TINYINT,
                                                      team1SeasonOppWins TINYINT,
                                                      team2SeasonOppWins TINYINT,
                                                      team1SeasonOppLoss TINYINT,
                                                      team2SeasonOppLoss TINYINT,
                                                      team1SeasonOppTie TINYINT,
                                                      team2SeasonOppTie TINYINT,
                                                      team1LifetimeOppWins TINYINT,
                                                      team2LifetimeOppWins TINYINT,
                                                      team1LifetimeOppLoss TINYINT,
                                                      team2LifetimeOppLoss TINYINT,
                                                      team1LifetimeOppTie TINYINT,
                                                      team2LifetimeOppTie TINYINT)''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS team (id INTEGER PRIMARY KEY AUTOINCREMENT, name TINYTEXT)''')

if __name__ == "__main__":
    exploreFile()
