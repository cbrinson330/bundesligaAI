import sqlite3
import tensorflow as tf
import numpy as np
from dateutil import parser
from datetime import datetime as dt

OUTCOMES = ['Loss', 'Tie', 'Win']

def load_data():
  """Returns the iris dataset as (train_x, train_y), (test_x, test_y)."""
  conn = sqlite3.connect('matches.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM match')

  allGames = cursor.fetchall()
  gameCount = int(len(allGames))
  #Train Arrays
  labels = []
  team1GoalsScoredThiSseason  = []
  team2GoalsScoredThisSeason = []
  team1GoalsAllowedThisSeason = []
  team2GoalsAllowedThisSeason = []
  team1GoalsScoredThisSeasonOpponent =  []
  team2GoalsScoredThisSeasonOpponent = []
  team1GoalsAllowedThisSeasonOpponent = [] 
  team2GoalsAllowedThisSeasonOpponent = [] 
  team1LifetimeGoalsScoredOpponent = [] 
  team2LifetimeGoalsScoredOpponent = [] 
  team1LifetimeGoalsAllowedOpponent = [] 
  team2LifetimeGoalsAllowedOpponent = []
  team1SeasonWins = [] 
  team2SeasonWins = [] 
  team1SeasonLoss = [] 
  team2SeasonLoss = [] 
  team1SeasonTie = [] 
  team2SeasonTie = [] 
  team1SeasonOppWins = [] 
  team2SeasonOppWins = [] 
  team1SeasonOppLoss = [] 
  team2SeasonOppLoss = [] 
  team1SeasonOppTie = [] 
  team2SeasonOppTie = [] 
  team1LifetimeOppWins = [] 
  team2LifetimeOppWins = [] 
  team1LifetimeOppLoss = [] 
  team2LifetimeOppLoss = [] 
  team1LifetimeOppTie = []
  team2LifetimeOppTie = []

  # Test Arrays
  testLabels = []
  testTeam1GoalsScoredThiSseason  = []
  testTeam2GoalsScoredThisSeason = []
  testTeam1GoalsAllowedThisSeason = []
  testTeam2GoalsAllowedThisSeason = []
  testTeam1GoalsScoredThisSeasonOpponent = []
  testTeam2GoalsScoredThisSeasonOpponent = []
  testTeam1GoalsAllowedThisSeasonOpponent = []
  testTeam2GoalsAllowedThisSeasonOpponent = []
  testTeam1LifetimeGoalsScoredOpponent = []
  testTeam2LifetimeGoalsScoredOpponent = []
  testTeam1LifetimeGoalsAllowedOpponent = []
  testTeam2LifetimeGoalsAllowedOpponent = []
  testTeam1SeasonWins = [] 
  testTeam2SeasonWins = [] 
  testTeam1SeasonLoss = [] 
  testTeam2SeasonLoss = [] 
  testTeam1SeasonTie = []
  testTeam2SeasonTie = []
  testTeam1SeasonOppWins = [] 
  testTeam2SeasonOppWins = [] 
  testTeam1SeasonOppLoss = [] 
  testTeam2SeasonOppLoss = [] 
  testTeam1SeasonOppTie = []
  testTeam2SeasonOppTie = []
  testTeam1LifetimeOppWins = []
  testTeam2LifetimeOppWins = []
  testTeam1LifetimeOppLoss = []
  testTeam2LifetimeOppLoss = []
  testTeam1LifetimeOppTie = []
  testTeam2LifetimeOppTie = []
  i = 0

  for game in allGames:
    date = dt.strptime(game[2], "%Y-%m-%d")
    cutoffDate = dt.strptime('2017-08-01', "%Y-%m-%d")
    curDate = now.strftime("%Y-%m-%d)

    if date < cutoffDate and date < curDate:
      team1GoalsScoredThiSseason.append(int(game[12]))
      team2GoalsScoredThisSeason.append(int(game[13]))
      team1GoalsAllowedThisSeason.append(int(game[13]))
      team2GoalsAllowedThisSeason.append(int(game[14]))
      team1GoalsScoredThisSeasonOpponent.append(int(game[15]))
      team2GoalsScoredThisSeasonOpponent.append(int(game[16]))
      team1GoalsAllowedThisSeasonOpponent.append(int(game[17]))
      team2GoalsAllowedThisSeasonOpponent.append(int(game[18]))
      team1LifetimeGoalsScoredOpponent.append(int(game[19]))
      team2LifetimeGoalsScoredOpponent.append(int(game[20]))
      team1LifetimeGoalsAllowedOpponent.append(int(game[21]))
      team2LifetimeGoalsAllowedOpponent.append(int(game[22]))
      team1SeasonWins.append(int(game[23]))
      team2SeasonWins.append(int(game[24]))
      team1SeasonLoss.append(int(game[25]))
      team2SeasonLoss.append(int(game[26]))
      team1SeasonTie.append(int(game[27]))
      team2SeasonTie.append(int(game[28]))
      team1SeasonOppWins.append(int(game[29]))
      team2SeasonOppWins.append(int(game[30]))
      team1SeasonOppLoss.append(int(game[31]))
      team2SeasonOppLoss.append(int(game[32]))
      team1SeasonOppTie.append(int(game[33]))
      team2SeasonOppTie.append(int(game[34]))
      team1LifetimeOppWins.append(int(game[35]))
      team2LifetimeOppWins.append(int(game[36]))
      team1LifetimeOppLoss.append(int(game[37]))
      team2LifetimeOppLoss.append(int(game[38]))
      team1LifetimeOppTie.append(int(game[39]))
      team2LifetimeOppTie.append(int(game[40]))

      labels.append(int(game[8]))
    elif date < curDate:
      testTeam1GoalsScoredThiSseason.append(int(game[12]))
      testTeam2GoalsScoredThisSeason.append(int(game[13]))
      testTeam1GoalsAllowedThisSeason.append(int(game[13]))
      testTeam2GoalsAllowedThisSeason.append(int(game[14]))
      testTeam1GoalsScoredThisSeasonOpponent.append(int(game[15]))
      testTeam2GoalsScoredThisSeasonOpponent.append(int(game[16]))
      testTeam1GoalsAllowedThisSeasonOpponent.append(int(game[17]))
      testTeam2GoalsAllowedThisSeasonOpponent.append(int(game[18]))
      testTeam1LifetimeGoalsScoredOpponent.append(int(game[19]))
      testTeam2LifetimeGoalsScoredOpponent.append(int(game[20]))
      testTeam1LifetimeGoalsAllowedOpponent.append(int(game[21]))
      testTeam2LifetimeGoalsAllowedOpponent.append(int(game[22]))
      testTeam1SeasonWins.append(int(game[23]))
      testTeam2SeasonWins.append(int(game[24]))
      testTeam1SeasonLoss.append(int(game[25]))
      testTeam2SeasonLoss.append(int(game[26]))
      testTeam1SeasonTie.append(int(game[27]))
      testTeam2SeasonTie.append(int(game[28]))
      testTeam1SeasonOppWins.append(int(game[29]))
      testTeam2SeasonOppWins.append(int(game[30]))
      testTeam1SeasonOppLoss.append(int(game[31]))
      testTeam2SeasonOppLoss.append(int(game[32]))
      testTeam1SeasonOppTie.append(int(game[33]))
      testTeam2SeasonOppTie.append(int(game[34]))
      testTeam1LifetimeOppWins.append(int(game[35]))
      testTeam2LifetimeOppWins.append(int(game[36]))
      testTeam1LifetimeOppLoss.append(int(game[37]))
      testTeam2LifetimeOppLoss.append(int(game[38]))
      testTeam1LifetimeOppTie.append(int(game[39]))
      testTeam2LifetimeOppTie.append(int(game[40]))

      testLabels.append(int(game[8]))

    i += 1

  features = {
    'team1GoalsScoredThiSseason': team1GoalsScoredThiSseason,
    'team2GoalsScoredThisSeason': team2GoalsScoredThisSeason,
    'team1GoalsAllowedThisSeason': team1GoalsAllowedThisSeason,
    'team2GoalsAllowedThisSeason': team2GoalsAllowedThisSeason,
    'team1GoalsScoredThisSeasonOpponent': team1GoalsScoredThisSeasonOpponent,
    'team2GoalsScoredThisSeasonOpponent': team2GoalsScoredThisSeasonOpponent,
    'team1GoalsAllowedThisSeasonOpponent': team1GoalsAllowedThisSeasonOpponent,
    'team2GoalsAllowedThisSeasonOpponent': team2GoalsAllowedThisSeasonOpponent,
    'team1LifetimeGoalsScoredOpponent': team1LifetimeGoalsScoredOpponent,
    'team2LifetimeGoalsScoredOpponent': team2LifetimeGoalsScoredOpponent,
    'team1LifetimeGoalsAllowedOpponent': team1LifetimeGoalsAllowedOpponent,
    'team2LifetimeGoalsAllowedOpponent': team2LifetimeGoalsAllowedOpponent,
    'team1SeasonWins': team1SeasonWins,
    'team2SeasonWins': team2SeasonWins,
    'team1SeasonLoss': team1SeasonLoss,
    'team2SeasonLoss': team2SeasonLoss,
    'team1SeasonTie': team1SeasonTie,
    'team2SeasonTie': team2SeasonTie,
    'team1SeasonOppWins': team1SeasonOppWins,
    'team2SeasonOppWins': team2SeasonOppWins,
    'team1SeasonOppLoss': team1SeasonOppLoss,
    'team2SeasonOppLoss': team2SeasonOppLoss,
    'team1SeasonOppTie': team1SeasonOppTie,
    'team2SeasonOppTie': team2SeasonOppTie,
    'team1LifetimeOppWins': team1LifetimeOppWins,
    'team2LifetimeOppWins': team2LifetimeOppWins,
    'team1LifetimeOppLoss': team1LifetimeOppLoss,
    'team2LifetimeOppLoss': team2LifetimeOppLoss,
    'team1LifetimeOppTie': team1LifetimeOppTie,
    'team2LifetimeOppTie': team2LifetimeOppTie
  }
  
  testFeatures = {
    'team1GoalsScoredThiSseason': testTeam1GoalsScoredThiSseason,
    'team2GoalsScoredThisSeason': testTeam2GoalsScoredThisSeason,
    'team1GoalsAllowedThisSeason': testTeam1GoalsAllowedThisSeason,
    'team2GoalsAllowedThisSeason': testTeam2GoalsAllowedThisSeason,
    'team1GoalsScoredThisSeasonOpponent': testTeam1GoalsScoredThisSeasonOpponent,
    'team2GoalsScoredThisSeasonOpponent': testTeam2GoalsScoredThisSeasonOpponent,
    'team1GoalsAllowedThisSeasonOpponent': testTeam1GoalsAllowedThisSeasonOpponent,
    'team2GoalsAllowedThisSeasonOpponent': testTeam2GoalsAllowedThisSeasonOpponent,
    'team1LifetimeGoalsScoredOpponent': testTeam1LifetimeGoalsScoredOpponent,
    'team2LifetimeGoalsScoredOpponent': testTeam2LifetimeGoalsScoredOpponent,
    'team1LifetimeGoalsAllowedOpponent': testTeam1LifetimeGoalsAllowedOpponent,
    'team2LifetimeGoalsAllowedOpponent': testTeam2LifetimeGoalsAllowedOpponent,
    'team1SeasonWins': testTeam1SeasonWins,
    'team2SeasonWins': testTeam2SeasonWins,
    'team1SeasonLoss': testTeam1SeasonLoss,
    'team2SeasonLoss': testTeam2SeasonLoss,
    'team1SeasonTie': testTeam1SeasonTie,
    'team2SeasonTie': testTeam2SeasonTie,
    'team1SeasonOppWins': testTeam1SeasonOppWins,
    'team2SeasonOppWins': testTeam2SeasonOppWins,
    'team1SeasonOppLoss': testTeam1SeasonOppLoss,
    'team2SeasonOppLoss': testTeam2SeasonOppLoss,
    'team1SeasonOppTie': testTeam1SeasonOppTie,
    'team2SeasonOppTie': testTeam2SeasonOppTie,
    'team1LifetimeOppWins': testTeam1LifetimeOppWins,
    'team2LifetimeOppWins': testTeam2LifetimeOppWins,
    'team1LifetimeOppLoss': testTeam1LifetimeOppLoss,
    'team2LifetimeOppLoss': testTeam2LifetimeOppLoss,
    'team1LifetimeOppTie': testTeam1LifetimeOppTie,
    'team2LifetimeOppTie': testTeam2LifetimeOppTie
  }

  return (features, labels), (testFeatures, testLabels)

def train_input_fn(features, labels, batch_size):
  #labels = list(map(int, labels))
  """An input function for training"""
  # Convert the inputs to a Dataset.
  dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

  # Shuffle, repeat, and batch the examples.
  dataset = dataset.shuffle(1000).repeat().batch(batch_size)

  # Return the dataset.
  return dataset

def eval_input_fn(features, labels, batch_size):
  #labels = labels.astype(int)
  #labels = list(map(int, labels))
  """An input function for evaluation or prediction"""
  features=dict(features)
  if labels is None:
      # No labels, use only features.
      inputs = features
  else:
      inputs = (features, labels)

  # Convert the inputs to a Dataset.
  dataset = tf.data.Dataset.from_tensor_slices(inputs)

  # Batch the examples
  assert batch_size is not None, "batch_size must not be None"
  dataset = dataset.batch(batch_size)

  # Return the dataset.
  return dataset

def upcoming_games():
  conn = sqlite3.connect('matches.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM match')
  allGames = cursor.fetchall()

  team1GoalsScoredThiSseason  = []
  team2GoalsScoredThisSeason = []
  team1GoalsAllowedThisSeason = []
  team2GoalsAllowedThisSeason = []
  team1GoalsScoredThisSeasonOpponent =  []
  team2GoalsScoredThisSeasonOpponent = []
  team1GoalsAllowedThisSeasonOpponent = [] 
  team2GoalsAllowedThisSeasonOpponent = [] 
  team1LifetimeGoalsScoredOpponent = [] 
  team2LifetimeGoalsScoredOpponent = [] 
  team1LifetimeGoalsAllowedOpponent = [] 
  team2LifetimeGoalsAllowedOpponent = []
  team1SeasonWins = [] 
  team2SeasonWins = [] 
  team1SeasonLoss = [] 
  team2SeasonLoss = [] 
  team1SeasonTie = [] 
  team2SeasonTie = [] 
  team1SeasonOppWins = [] 
  team2SeasonOppWins = [] 
  team1SeasonOppLoss = [] 
  team2SeasonOppLoss = [] 
  team1SeasonOppTie = [] 
  team2SeasonOppTie = [] 
  team1LifetimeOppWins = [] 
  team2LifetimeOppWins = [] 
  team1LifetimeOppLoss = [] 
  team2LifetimeOppLoss = [] 
  team1LifetimeOppTie = []
  team2LifetimeOppTie = []

  for game in allGames:
    date = dt.strptime(game[2], "%Y-%m-%d")
    curDate = now.strftime("%Y-%m-%d)

    if date > curDate:
      team1GoalsScoredThiSseason.append(int(game[12]))
      team2GoalsScoredThisSeason.append(int(game[13]))
      team1GoalsAllowedThisSeason.append(int(game[13]))
      team2GoalsAllowedThisSeason.append(int(game[14]))
      team1GoalsScoredThisSeasonOpponent.append(int(game[15]))
      team2GoalsScoredThisSeasonOpponent.append(int(game[16]))
      team1GoalsAllowedThisSeasonOpponent.append(int(game[17]))
      team2GoalsAllowedThisSeasonOpponent.append(int(game[18]))
      team1LifetimeGoalsScoredOpponent.append(int(game[19]))
      team2LifetimeGoalsScoredOpponent.append(int(game[20]))
      team1LifetimeGoalsAllowedOpponent.append(int(game[21]))
      team2LifetimeGoalsAllowedOpponent.append(int(game[22]))
      team1SeasonWins.append(int(game[23]))
      team2SeasonWins.append(int(game[24]))
      team1SeasonLoss.append(int(game[25]))
      team2SeasonLoss.append(int(game[26]))
      team1SeasonTie.append(int(game[27]))
      team2SeasonTie.append(int(game[28]))
      team1SeasonOppWins.append(int(game[29]))
      team2SeasonOppWins.append(int(game[30]))
      team1SeasonOppLoss.append(int(game[31]))
      team2SeasonOppLoss.append(int(game[32]))
      team1SeasonOppTie.append(int(game[33]))
      team2SeasonOppTie.append(int(game[34]))
      team1LifetimeOppWins.append(int(game[35]))
      team2LifetimeOppWins.append(int(game[36]))
      team1LifetimeOppLoss.append(int(game[37]))
      team2LifetimeOppLoss.append(int(game[38]))
      team1LifetimeOppTie.append(int(game[39]))
      team2LifetimeOppTie.append(int(game[40]))

  features = {
    'team1GoalsScoredThiSseason': team1GoalsScoredThiSseason,
    'team2GoalsScoredThisSeason': team2GoalsScoredThisSeason,
    'team1GoalsAllowedThisSeason': team1GoalsAllowedThisSeason,
    'team2GoalsAllowedThisSeason': team2GoalsAllowedThisSeason,
    'team1GoalsScoredThisSeasonOpponent': team1GoalsScoredThisSeasonOpponent,
    'team2GoalsScoredThisSeasonOpponent': team2GoalsScoredThisSeasonOpponent,
    'team1GoalsAllowedThisSeasonOpponent': team1GoalsAllowedThisSeasonOpponent,
    'team2GoalsAllowedThisSeasonOpponent': team2GoalsAllowedThisSeasonOpponent,
    'team1LifetimeGoalsScoredOpponent': team1LifetimeGoalsScoredOpponent,
    'team2LifetimeGoalsScoredOpponent': team2LifetimeGoalsScoredOpponent,
    'team1LifetimeGoalsAllowedOpponent': team1LifetimeGoalsAllowedOpponent,
    'team2LifetimeGoalsAllowedOpponent': team2LifetimeGoalsAllowedOpponent,
    'team1SeasonWins': team1SeasonWins,
    'team2SeasonWins': team2SeasonWins,
    'team1SeasonLoss': team1SeasonLoss,
    'team2SeasonLoss': team2SeasonLoss,
    'team1SeasonTie': team1SeasonTie,
    'team2SeasonTie': team2SeasonTie,
    'team1SeasonOppWins': team1SeasonOppWins,
    'team2SeasonOppWins': team2SeasonOppWins,
    'team1SeasonOppLoss': team1SeasonOppLoss,
    'team2SeasonOppLoss': team2SeasonOppLoss,
    'team1SeasonOppTie': team1SeasonOppTie,
    'team2SeasonOppTie': team2SeasonOppTie,
    'team1LifetimeOppWins': team1LifetimeOppWins,
    'team2LifetimeOppWins': team2LifetimeOppWins,
    'team1LifetimeOppLoss': team1LifetimeOppLoss,
    'team2LifetimeOppLoss': team2LifetimeOppLoss,
    'team1LifetimeOppTie': team1LifetimeOppTie,
    'team2LifetimeOppTie': team2LifetimeOppTie
  }
  return features

getValuesForTeams(home, guest):
  # Home and guest values should be Id's
  if int(home) > 0 and int(guest) > 0:
    conn = sqlite3.connect('matches.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM match WHERE team1 = ' + home + ' AND team2 =' + guest)
    allGamesForTeam = cursor.fetchall()
    if len(allGamesForTeam) > 0:
      latestGame = allGamesForTeam[-1]

      features = {
        'team1GoalsScoredThiSseason': [int(latestGame[12])],
        'team2GoalsScoredThisSeason': [int(latestGame[13])],
        'team1GoalsAllowedThisSeason': [int(latestGame[14])],
        'team2GoalsAllowedThisSeason': [int(latestGame[15])],
        'team1GoalsScoredThisSeasonOpponent': [int(latestGame[16])],
        'team2GoalsScoredThisSeasonOpponent': [int(latestGame[17])],
        'team1GoalsAllowedThisSeasonOpponent': [int(latestGame[18])],
        'team2GoalsAllowedThisSeasonOpponent': [int(latestGame[19])],
        'team1LifetimeGoalsScoredOpponent': [int(latestGame[20])],
        'team2LifetimeGoalsScoredOpponent': [int(latestGame[21])],
        'team1LifetimeGoalsAllowedOpponent': [int(latestGame[22])],
        'team2LifetimeGoalsAllowedOpponent': [int(latestGame[23])],
        'team1SeasonWins': [int(latestGame[24])],
        'team2SeasonWins': [int(latestGame[25])],
        'team1SeasonLoss': [int(latestGame[26])],
        'team2SeasonLoss': [int(latestGame[27])],
        'team1SeasonTie': [int(latestGame[28])],
        'team2SeasonTie': [int(latestGame[29])],
        'team1SeasonOppWins': [int(latestGame[30])],
        'team2SeasonOppWins': [int(latestGame[31])],
        'team1SeasonOppLoss': [int(latestGame[32])],
        'team2SeasonOppLoss': [int(latestGame[33])],
        'team1SeasonOppTie': [int(latestGame[34])],
        'team2SeasonOppTie': [int(latestGame[35])],
        'team1LifetimeOppWins': [int(latestGame[36])],
        'team2LifetimeOppWins': [int(latestGame[37])],
        'team1LifetimeOppLoss': [int(latestGame[38])],
        'team2LifetimeOppLoss': [int(latestGame[39])],
        'team1LifetimeOppTie': [int(latestGame[40])],
        'team2LifetimeOppTie': [int(latestGame[41])]
      }
    return features
