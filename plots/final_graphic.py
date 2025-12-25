import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
import pickle

path = "/Users/ryderfried/Documents/2024-2025/Courses/Spring/CS109/pickle/store_dic.p"
with open(path, "rb") as f:
    store_dic = pickle.load(f)

# Example color map for different outcomes
color_map = {
    'foul': 'red',
    'tied': 'purple',
    'no foul': 'blue',
}

# RGB mapping for imshow
color_to_rgb = {
    'red': [1, 0, 0],
    'purple': [0.5, 0, 0.5],
    'blue': [0, 0, 1],
}

# Axis ranges
x_min, x_max = 1, 60       # Horizontal axis = Time Remaining
y_min, y_max = -10, 3     # Vertical axis = Point Differential

# Grid dimensions
height = y_max - y_min + 1
width = x_max - x_min + 1
grid_colors = np.empty((height, width), dtype=object)

# Fill the color grid
for y in range(y_min, y_max + 1):      # vertical (row)
    for x in range(x_min, x_max + 1):  # horizontal (column)
        key = (y, x)
        value = store_dic.get(key, {'better': 'no foul'})['better']
        color = color_map.get(value, 'gray')  # fallback for unknown keys
        row = y - y_min
        col = x - x_min
        grid_colors[row, col] = color

# Convert to RGB grid
rgb_grid = np.array([[color_to_rgb[c] for c in row] for row in grid_colors])

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Show the image with perfect grid alignment
ax.imshow(
    rgb_grid,
    origin='lower',
    interpolation='none',
    extent=[x_min - 0.5, x_max + 0.5, y_min - 0.5, y_max + 0.5]
)

# Draw a black rectangle grid over each square
for y in range(y_min, y_max + 1):
    for x in range(x_min, x_max + 1):
        rect = Rectangle((x - 0.5, y - 0.5), 1, 1,
                         linewidth=0.5, edgecolor='black', facecolor='none')
        rect.set_antialiased(False)  # Prevent blurring at edges
        ax.add_patch(rect)

# Axis labels and ticks
ax.set_xticks(range(x_min, x_max + 1, 5))
ax.set_yticks(range(y_min, y_max + 1, 1))
ax.set_xlabel('Time Remaining (seconds)', fontsize=14)
ax.set_ylabel('Point Differential', fontsize=14)
ax.set_title("Late Game Foul Decision Chart",fontsize=16)
ax.set_aspect('equal')  # Keep grid square
ax.grid(False)



# Legend
legend_patches = [
    mpatches.Patch(color='red', label='Foul'),
    mpatches.Patch(color='purple', label='No Difference'),
    mpatches.Patch(color='blue', label='No Foul'),
]
ax.legend(handles=legend_patches, title='Decision with Higher Win %', loc='upper right')

# Save high-quality image
fig.tight_layout()
fig.savefig("datasets/final_graphic.png", dpi=300, bbox_inches='tight')
plt.show()