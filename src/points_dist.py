#Concerning the outcome variable (pts), no points were scored in most of the possessions (59.6%). Of the remaining ones, 26.2% resulted in two points and 11.6% in
#three points. One-point possessions accounted only for 2.5% of the total number of
#possessions. This was due to the fact that two successful free throws (in one possession) were considered as two-point possessions. Finally, more than three points were
#scored in only 0.1% of the possessions.

# 0: 0.596
# 1: 0.025
# 2: 0.262
# 3: 0.116
# 4: 0.001

# https://www.basketball-reference.com/leagues/NBA_stats_per_poss.html
# TO: 12.6
# PTS: 114.5

# https://www.reddit.com/r/nba/comments/171fqih/13_unlikelybutplausible_predictions_what_are_yours/
#OREB%:

import random

def pointsPos():
  x = random.randint(1, 1000)
  # 12.6% of possessions are turnovers
  if x <= 126:
    return 0

  # 47% of posessions are missed shots
  elif x <= 596:
    
    # 44.166% chance of an offensive rebound
    y = random.random()
    if y <= 0.44166:
      return pointsPos()
    return 0
  # 2.5% of possessions end in 1 point 
  elif x <= 596 + 25:
    
    # Asssuming shooting 2 shots, 50% chance of missing first making second
    y = random.randint(1, 2)
    if y == 1:
      return 1
    # 50% chance if making first and making second
    else:
      # 44.166% chance of an offensive rebound
      z = random.random()
      if z <= 0.44166:
        return 1 + pointsPos()
      else:
        return 1
  # 26.2% chance of possession ending in 2 points
  elif x <= 596 + 25 + 262:
    return 2
  # 11.6% chance of possession ending in 2 points
  elif x <= 596 + 25 + 262 + 116:
    return 3
  # The rest is a four point possession
  else:
    return 4

# Building Categorical Distribution (including offensive Rebounds)
sum = 0
tot_res = [0] * 8
num_trials = 1000000
for _ in range(num_trials):
  pts = min(pointsPos(), 7)
  tot_res[pts] += 1
  res_per_pos = [pts / num_trials for pts in tot_res]
