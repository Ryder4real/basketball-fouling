import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from scipy import stats
from collections import defaultdict
import pickle

# Easy access to mean and std_dev
def normal_param(df_sec_counts):
  values = np.array(list(df_sec_counts.keys()))
  counts = np.array(list(df_sec_counts.values()))

  norm_mean = np.average(values, weights=counts)
  norm_variance = np.average((values - norm_mean)**2, weights=counts)
  norm_std_dev = np.sqrt(norm_variance)

  return (norm_mean, norm_std_dev)

def get_mean_std():
    path = "datasets/dict_sec_counts.p"
    with open(path, "rb") as f:
        data = pickle.load(f)
    return normal_param(data)
