import numpy as np
from src.points_dist import res_per_pos
def ft_result():
   ft = int(sum(np.random.binomial(1, 0.78, size=2)))
   return ft

def one_pos_points(decision):
  # If defense fouls
  if decision:
    return ft_result()
  
  categories = [0, 1, 2, 3, 4, 5, 6, 7]
  probabilities = res_per_pos
  sample = np.random.choice(categories, p = probabilities)
  return int(sample)