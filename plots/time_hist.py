import pandas as pd
import matplotlib.pyplot as plt
import pickle

with open("datasets/dict_sec_counts.p", "rb") as f:
        total_counts = pickle.load(f)
df = pd.DataFrame(list(total_counts.items()), columns=['sec', 'count'])

ax = df.plot.bar(x='sec', y='count', legend=False, title='Distribution of Length of Possessions', fontsize=12)

ax.set_xlabel('Length of Possessions (seconds)', fontsize=14)
ax.set_ylabel('Counts', fontsize=14)
ax.xaxis.labelpad = 10

# Set x-ticks every 5 seconds
ax.set_xticks(range(0, 66, 5))  # Assuming sec ranges 0–65
ax.set_xticklabels(range(0, 66, 5), rotation=0)  # Optional: no angle
ax.set_title('Distribution of Length of Possessions', fontsize=16)

# Save the figure
plt.savefig('plots/time_hist', dpi=300)