import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Grid size
grid_size = 40
radius = grid_size // 2
amt = 5  # Initial amt value

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)
center = (grid_size // 2, grid_size // 2)

# Function to update the plot
def update(val):
    radius = int(radius_slider.val)
    amt = int(amt_slider.val)
    grid = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            if abs((i - center[0])**2 + (j - center[1])**2 - radius**2) <= amt:
                grid[i, j] = 1
    ax.clear()
    ax.imshow(grid, cmap='gray', interpolation='nearest')
    ax.axis('off')
    fig.canvas.draw_idle()

# Initial plot
radius_slider_ax = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgray')
radius_slider = Slider(radius_slider_ax, 'Radius', 0, grid_size // 2, valinit=radius, valstep=1)
amt_slider_ax = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgray')
amt_slider = Slider(amt_slider_ax, 'Amt', 0, 20, valinit=amt, valstep=1)

radius_slider.on_changed(update)
amt_slider.on_changed(update)

update(radius)
plt.show()

