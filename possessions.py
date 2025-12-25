from pos_points import ft_result, one_pos_points
from pos_time import one_pos_time

def off_pos(score_diff, time_left, decision):
  # time_left
  new_time_left = time_left - one_pos_time("off", score_diff, time_left, decision)
  # Ran out of time
  if new_time_left <= 0:
    return(score_diff, new_time_left)
  # otherwise
  new_score_diff = score_diff + one_pos_points(decision)
  return(new_score_diff, new_time_left)

# Test Example
off_pos(7, 10, True)

def def_pos(score_diff, time_left, foul_decision):
    # time_left
    new_time_left = time_left - one_pos_time("def", score_diff, time_left, foul_decision)
    # Ran out of time
    if new_time_left <= 0:
      return(score_diff, new_time_left)
    # Otherwise
    new_score_diff = score_diff - one_pos_points(foul_decision)
    return(new_score_diff, new_time_left)

# Test Example
def_pos(1, 3, True)