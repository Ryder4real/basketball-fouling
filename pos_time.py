import numpy as np
import pickle

from time_dist import get_mean_std
mean, std_dev = get_mean_std()

def one_pos_time(pos, score_diff, time_left, decision):
  # If defense decides to foul
  if decision:
    return 0.51

  # If offense can run out the clock
  if (pos == "off" and score_diff > 0 and time_left <=24) or (pos == "def" and score_diff < 0 and time_left <= 24):
    return time_left

  # If offense is losing, time of possession folows a normal distribution with "coef" representing the urgency of the team
  # Urgency is time left in game / shot clock (with minimum being 5/24)

  coef = 1
  if (pos == "off" and score_diff < 0) or (pos == "def" and score_diff > 0):
    if time_left >= 24:
      coef = 1
    elif time_left >= 5:
      coef = time_left / 24
    else:
      coef = 5 / 24
  elif (pos == "off" and score_diff > 0) or (pos == "def" and score_diff < 0):
    if time_left > 24 and time_left < 40:
      coef = -0.03933 * time_left +2.5732

  result = (np.random.normal(mean * coef, std_dev * coef))
  # possession cannot take less than 0.51 seconds
  return max(result, 0.51)

# Test Example
one_pos_time("def", -1, 25, False)