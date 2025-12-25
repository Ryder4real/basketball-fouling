import pickle
from possessions import off_pos, def_pos

n_sim = 20000
store_dic = {}

# Recrusive sim formula
def sim(score_diff, time_left, decision):
  # Starter variables
  num_won = 0
  num_tied = 0
  in_dic = 0
  this_sim_dic = {}
  total_win_prob = 0
  sim_to_end = False

  for _ in range(n_sim):
    time = time_left
    after_pos = (score_diff, time_left)
    # With time left in game:
    while time > 0:
      sim_to_end = False
      situation = (after_pos[0], round(after_pos[1]))
      # If time left/score diff has already been simulated:
      if situation in store_dic:
        win_prob = store_dic[situation]["win prob"]
        if win_prob not in this_sim_dic:
          this_sim_dic[win_prob] = 0
        in_dic += 1
        this_sim_dic[win_prob] += 1
        sim_to_end = True
        break

      else:
        # Run one defensive possession
        if time > 0:
          after_pos = def_pos(after_pos[0], after_pos[1], decision)
          time = after_pos[1]
        # If not time left - end sim
        if time <= 0:
          break

        # New Situation
        situation = (after_pos[0] * -1, round(after_pos[1]))
        # See if situation has been simulated already
        if situation in store_dic:
          win_prob = 1 - store_dic[situation]["win prob"]
          if win_prob not in this_sim_dic:
            this_sim_dic[win_prob] = 0
          in_dic += 1
          this_sim_dic[win_prob] += 1
          sim_to_end = True
          break
        # If new situation, and situation will come up again, then keep simming
        elif abs(after_pos[0]) < 10 and abs(after_pos[0]) > 0:
          win_prob = 1 - foul_no_foul_sim(situation[0], situation[1])
          if win_prob not in this_sim_dic:
            this_sim_dic[win_prob] = 0
          in_dic += 1
          this_sim_dic[win_prob] += 1
          sim_to_end = True
          break

        # If new situation but not a close game, then don't foul
        after_pos = off_pos(after_pos[0], after_pos[1], False)
        time = after_pos[1]
    # If win prob has not been saved (and goes until the game is over)
    if sim_to_end == False:
      final_score_diff = after_pos[0]
      if final_score_diff > 0:
        num_won += 1
      elif final_score_diff == 0:
        num_tied += 1
  # Calculate overall win prob
  for win_prob in this_sim_dic:
    total_win_prob += (this_sim_dic[win_prob] / n_sim) * win_prob
  return total_win_prob + num_won / n_sim + 0.5 * (num_tied / n_sim)


# Run the simulation both with fouling and not fouling, and store the better outcome
def foul_no_foul_sim(score, time):
  tup = (score, time)
  with_foul = sim(score, time, True)
  no_foul = sim(score, time, False)
  store_dic[tup] = {}
  store_dic[tup]["foul"] = with_foul
  store_dic[tup]["no foul"] = no_foul
  store_dic[tup]["win prob"] = max(with_foul, no_foul)

  if no_foul > with_foul:
    store_dic[tup]["better"] = "no foul"
  elif no_foul == with_foul:
    store_dic[tup]["better"] = "tied"
  else:
    store_dic[tup]["better"] = "foul"

  return store_dic[tup]["win prob"]

# Actually run it for time left and score outcomes
for j in range(1, 61):
  print(j) # track progress
  for i in range(-15, 6):
    score, time = i, j
    with_foul = sim(score, time, True)
    no_foul = sim(score, time, False)
    tup = (score, time)
    store_dic[tup] = {}
    store_dic[tup]["foul"] = with_foul
    store_dic[tup]["no foul"] = no_foul
    store_dic[tup]["win prob"] = max(with_foul, no_foul)

    if no_foul > with_foul:
      store_dic[tup]["better"] = "no foul"
    elif no_foul == with_foul:
      store_dic[tup]["better"] = "tied"
    else:
      store_dic[tup]["better"] = "foul"

# Save dictionary
with open("datasets/store_dict.p", "wb") as file_handle:
    pickle.dump(store_dic, file_handle)