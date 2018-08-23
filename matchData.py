import sqlite3
import tensorflow as tf
import numpy as np


# TODO update load_data function to work
# Need to get to something like this
# features = {'SepalLength': np.array([6.4, 5.0]),
#                'SepalWidth':  np.array([2.8, 2.3]),
#                'PetalLength': np.array([5.6, 3.3]),
#                'PetalWidth':  np.array([2.2, 1.0])}
#    labels = np.array([2, 1])
#    return features, labels

def load_data():
  """Returns the iris dataset as (train_x, train_y), (test_x, test_y)."""
  conn = sqlite3.connect('matches.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM match')

  allGames = cursor.fetchall()
  gameCount = int(len(allGames))
  #Train Arrays
  labels = np.zeros(gameCount)
  team1GoalsScoredThiSseason  = np.zeros(gameCount)
  team2GoalsScoredThisSeason = np.zeros(gameCount)
  team1GoalsAllowedThisSeason = np.zeros(gameCount)
  team2GoalsAllowedThisSeason = np.zeros(gameCount)
  team1GoalsScoredThisSeasonOpponent = np.zeros(gameCount)
  team2GoalsScoredThisSeasonOpponent = np.zeros(gameCount)
  team1GoalsAllowedThisSeasonOpponent = np.zeros(gameCount)
  team2GoalsAllowedThisSeasonOpponent = np.zeros(gameCount)
  team1LifetimeGoalsScoredOpponent = np.zeros(gameCount)
  team2LifetimeGoalsScoredOpponent = np.zeros(gameCount)
  team1LifetimeGoalsAllowedOpponent = np.zeros(gameCount) 
  team2LifetimeGoalsAllowedOpponent = np.zeros(gameCount)
  team1SeasonWins = np.zeros(gameCount)
  team2SeasonWins = np.zeros(gameCount)
  team1SeasonLoss = np.zeros(gameCount)
  team2SeasonLoss = np.zeros(gameCount)
  team1SeasonTie = np.zeros(gameCount)
  team2SeasonTie = np.zeros(gameCount)
  team1SeasonOppWins = np.zeros(gameCount)
  team2SeasonOppWins = np.zeros(gameCount)
  team1SeasonOppLoss = np.zeros(gameCount)
  team2SeasonOppLoss = np.zeros(gameCount)
  team1SeasonOppTie = np.zeros(gameCount)
  team2SeasonOppTie = np.zeros(gameCount)
  team1LifetimeOppWins = np.zeros(gameCount)
  team2LifetimeOppWins = np.zeros(gameCount)
  team1LifetimeOppLoss = np.zeros(gameCount)
  team2LifetimeOppLoss = np.zeros(gameCount)
  team1LifetimeOppTie = np.zeros(gameCount)
  team2LifetimeOppTie = np.zeros(gameCount)

  # Test Arrays
  testLabels = np.zeros(gameCount)
  testTeam1GoalsScoredThiSseason  = np.zeros(gameCount)
  testTeam2GoalsScoredThisSeason = np.zeros(gameCount)
  testTeam1GoalsAllowedThisSeason = np.zeros(gameCount)
  testTeam2GoalsAllowedThisSeason = np.zeros(gameCount)
  testTeam1GoalsScoredThisSeasonOpponent = np.zeros(gameCount)
  testTeam2GoalsScoredThisSeasonOpponent = np.zeros(gameCount)
  testTeam1GoalsAllowedThisSeasonOpponent = np.zeros(gameCount)
  testTeam2GoalsAllowedThisSeasonOpponent = np.zeros(gameCount)
  testTeam1LifetimeGoalsScoredOpponent = np.zeros(gameCount)
  testTeam2LifetimeGoalsScoredOpponent = np.zeros(gameCount)
  testTeam1LifetimeGoalsAllowedOpponent = np.zeros(gameCount)
  testTeam2LifetimeGoalsAllowedOpponent = np.zeros(gameCount)
  testTeam1SeasonWins = np.zeros(gameCount)
  testTeam2SeasonWins = np.zeros(gameCount)
  testTeam1SeasonLoss = np.zeros(gameCount)
  testTeam2SeasonLoss = np.zeros(gameCount)
  testTeam1SeasonTie = np.zeros(gameCount)
  testTeam2SeasonTie = np.zeros(gameCount)
  testTeam1SeasonOppWins = np.zeros(gameCount)
  testTeam2SeasonOppWins = np.zeros(gameCount)
  testTeam1SeasonOppLoss = np.zeros(gameCount)
  testTeam2SeasonOppLoss = np.zeros(gameCount)
  testTeam1SeasonOppTie = np.zeros(gameCount)
  testTeam2SeasonOppTie = np.zeros(gameCount)
  testTeam1LifetimeOppWins = np.zeros(gameCount)
  testTeam2LifetimeOppWins = np.zeros(gameCount)
  testTeam1LifetimeOppLoss = np.zeros(gameCount)
  testTeam2LifetimeOppLoss = np.zeros(gameCount)
  testTeam1LifetimeOppTie = np.zeros(gameCount)
  testTeam2LifetimeOppTie = np.zeros(gameCount)
  i = 0

  for game in allGames:
    if game[1] != '2017':
      team1GoalsScoredThiSseason[i] = int(game[12])
      team2GoalsScoredThisSeason[i] = int(game[13]) 
      team1GoalsAllowedThisSeason[i] = int(game[13])
      team2GoalsAllowedThisSeason[i] = int(game[14]) 
      team1GoalsScoredThisSeasonOpponent[i] = int(game[15]) 
      team2GoalsScoredThisSeasonOpponent[i] = int(game[16])
      team1GoalsAllowedThisSeasonOpponent[i] = int(game[17])
      team2GoalsAllowedThisSeasonOpponent[i] = int(game[18]) 
      team1LifetimeGoalsScoredOpponent[i] = int(game[19]) 
      team2LifetimeGoalsScoredOpponent[i] = int(game[20]) 
      team1LifetimeGoalsAllowedOpponent[i] = int(game[21]) 
      team2LifetimeGoalsAllowedOpponent[i] = int(game[22]) 
      team1SeasonWins[i] = int(game[23]) 
      team2SeasonWins[i] = int(game[24]) 
      team1SeasonLoss[i] = int(game[25]) 
      team2SeasonLoss[i] = int(game[26])
      team1SeasonTie[i] = int(game[27]) 
      team2SeasonTie[i] = int(game[28]) 
      team1SeasonOppWins[i] = int(game[29]) 
      team2SeasonOppWins[i] = int(game[30]) 
      team1SeasonOppLoss[i] = int(game[31]) 
      team2SeasonOppLoss[i] = int(game[32]) 
      team1SeasonOppTie[i] = int(game[33])
      team2SeasonOppTie[i] = int(game[34]) 
      team1LifetimeOppWins[i] = int(game[35])
      team2LifetimeOppWins[i] = int(game[36]) 
      team1LifetimeOppLoss[i] = int(game[37])
      team2LifetimeOppLoss[i] = int(game[38]) 
      team1LifetimeOppTie[i] = int(game[39]) 
      team2LifetimeOppTie[i] = int(game[40]) 

      labels[i] = int(game[8])
    else:
      testTeam1GoalsScoredThiSseason[i] = int(game[12])
      testTeam2GoalsScoredThisSeason[i] = int(game[13]) 
      testTeam1GoalsAllowedThisSeason[i] = int(game[13])
      testTeam2GoalsAllowedThisSeason[i] = int(game[14]) 
      testTeam1GoalsScoredThisSeasonOpponent[i] = int(game[15]) 
      testTeam2GoalsScoredThisSeasonOpponent[i] = int(game[16])
      testTeam1GoalsAllowedThisSeasonOpponent[i] = int(game[17])
      testTeam2GoalsAllowedThisSeasonOpponent[i] = int(game[18]) 
      testTeam1LifetimeGoalsScoredOpponent[i] = int(game[19]) 
      testTeam2LifetimeGoalsScoredOpponent[i] = int(game[20]) 
      testTeam1LifetimeGoalsAllowedOpponent[i] = int(game[21]) 
      testTeam2LifetimeGoalsAllowedOpponent[i] = int(game[22]) 
      testTeam1SeasonWins[i] = int(game[23]) 
      testTeam2SeasonWins[i] = int(game[24]) 
      testTeam1SeasonLoss[i] = int(game[25]) 
      testTeam2SeasonLoss[i] = int(game[26])
      testTeam1SeasonTie[i] = int(game[27]) 
      testTeam2SeasonTie[i] = int(game[28]) 
      testTeam1SeasonOppWins[i] = int(game[29]) 
      testTeam2SeasonOppWins[i] = int(game[30]) 
      testTeam1SeasonOppLoss[i] = int(game[31]) 
      testTeam2SeasonOppLoss[i] = int(game[32]) 
      testTeam1SeasonOppTie[i] = int(game[33])
      testTeam2SeasonOppTie[i] = int(game[34]) 
      testTeam1LifetimeOppWins[i] = int(game[35])
      testTeam2LifetimeOppWins[i] = int(game[36]) 
      testTeam1LifetimeOppLoss[i] = int(game[37])
      testTeam2LifetimeOppLoss[i] = int(game[38]) 
      testTeam1LifetimeOppTie[i] = int(game[39]) 
      testTeam2LifetimeOppTie[i] = int(game[40]) 

      testLabels[i] = int(game[8])

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

  labels.astype(int)
  testLabels.astype(int)

  return (features, labels), (testFeatures, testLabels)

  
# features = {'SepalLength': np.array([6.4, 5.0]),
#                'SepalWidth':  np.array([2.8, 2.3]),
#                'PetalLength': np.array([5.6, 3.3]),
#                'PetalWidth':  np.array([2.2, 1.0])}
#    labels = np.array([2, 1])
#    return features, labels


  # train_path, test_path = maybe_download()
  # train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
  #train_x, train_y = train, train.pop(y_name)
  
  #test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
  #test_x, test_y = test, test.pop(y_name)
  
  #return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size):
  labels = labels.astype(int)
  """An input function for training"""
  # Convert the inputs to a Dataset.
  dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

  # Shuffle, repeat, and batch the examples.
  dataset = dataset.shuffle(1000).repeat().batch(batch_size)

  # Return the dataset.
  return dataset


def eval_input_fn(features, labels, batch_size):
  labels = labels.astype(int)
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
