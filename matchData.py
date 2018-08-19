import sqlite3
import tensorflow as tf

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
  cursor.execute('SELECT * FROM match)

  allGames = cursor.fetchall()
  team1goalsScoredThisSeason = []
  team2goalsAllowedThisSeason = []


  for game in allGames:
    

  # train_path, test_path = maybe_download()
  train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
  train_x, train_y = train, train.pop(y_name)
  
  test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
  test_x, test_y = test, test.pop(y_name)
  
  return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size):
  """An input function for training"""
  # Convert the inputs to a Dataset.
  dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

  # Shuffle, repeat, and batch the examples.
  dataset = dataset.shuffle(1000).repeat().batch(batch_size)

  # Return the dataset.
  return dataset


def eval_input_fn(features, labels, batch_size):
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
