import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib.lines import Line2D
import pickle

# Make QQ Plot
path = "datasets/dict_sec_counts.p"
with open(path, "rb") as f:
        total_counts = pickle.load(f)
df_sec_counts = pd.DataFrame(list(total_counts.items()), columns=['sec', 'count'])
data = df_sec_counts['sec'].dropna().sort_values()

# Z-score the data
data_z = stats.zscore(data)

# Get theoretical quantiles from normal distribution
n = len(data_z)
data_q = np.sort(data_z)
# Theoretical quantiles from standard normal
theoretical_q = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)

# Fit line to quantiles
slope, intercept, r_value, p_value, std_err = stats.linregress(theoretical_q, data_q)
r_squared = r_value ** 2

# Plot
plt.plot(theoretical_q, data_q, 'o', label='Data Points')
plt.plot(theoretical_q, slope * theoretical_q + intercept, 'r-', label='Fitted Line')

plt.xlabel('Theoretical Quantiles (Standard Normal)', fontsize=14)
plt.ylabel('Possession Data Quantiles', fontsize=14)
plt.title('Normal Q-Q Plot', fontsize=16)

# R² annotation
plt.text(0.05, 0.95, f"$R^2 = {r_squared:.4f}$", transform=plt.gca().transAxes,
         verticalalignment='top', fontsize=12, bbox=dict(boxstyle="round", fc="white", ec="gray"))

# Legend
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Data Points',
           markerfacecolor='blue', markersize=8),
    Line2D([0], [0], color='red', lw=2, label='Fitted Line')
]
plt.legend(handles=legend_elements, loc='lower right')

# Save and show
plt.tight_layout()
plt.savefig("norm_qq_plot.png", dpi=300)
plt.show()