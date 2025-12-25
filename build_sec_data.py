import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from scipy import stats
from collections import defaultdict
import pickle


url = "https://api.pbpstats.com/get-possession-length-frequency/nba"
params = {
    "Season": "2024-25",
    "SeasonType": "Regular Season",
    "PossessionType": "Offense", # Offense or Defense
    "TimeType": "IncludeSecondChances", # IncludeSecondChances or ExcludeSecondChances
    "StartType": "All"
}
response = requests.get(url, params=params)
response_json = response.json()
list_of_teams = response_json["results"]

dd_total_counts = defaultdict(int)

# Build data for a histagraph of posession length 
for team, sec_counts in list_of_teams.items():
    for item in sec_counts:
        dd_total_counts[item['length']] += item['count']

# Convert defaultdict to regular dict if you want
total_counts = dict(dd_total_counts)

# Save dictionary as pickle
with open("/Users/ryderfried/Documents/2024-2025/Courses/Spring/CS109/pickle/dic_sec_counts.p", "wb") as file_handle:
    pickle.dump(total_counts, file_handle)

# Save as CSV file:
df_sec_counts = pd.DataFrame(list(total_counts.items()), columns=['sec', 'count'])
df_sec_counts.to_csv("/Users/ryderfried/Documents/2024-2025/Courses/Spring/CS109/df_sec_counts.csv", index=False)