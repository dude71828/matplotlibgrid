
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import time
import random

# Grid size
grid_size = 100
paused = False

def on_click(event):
    global paused
    paused = not paused

# Initialize random grid
grid = np.random.randint(0, 2, (grid_size, grid_size))

# Function to apply Game of Life rules
def update_grid1(grid):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            # Count live neighbors, ignoring wrap-around
            neighbors = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    ni, nj = i + x, j + y
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        neighbors += grid[ni, nj]
            # Apply rules
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

def update_grid2(grid):
    new_grid = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j]==1:
                if i>=1:
                    if grid[i-1][j]==1:
                        new_grid[i][j]=1
                    else:
                        new_grid[i-1][j]=1
                else:
                    new_grid[i][j]=1
    return new_grid

def update_grid3(grid):
    new_grid = np.zeros((grid_size, grid_size))
    count = np.zeros((grid_size, grid_size))
    lst = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j]==1:
                s = random.choice(lst)
                count[(i+s[0])%grid_size][(j+s[1])%grid_size] += 1
            if grid[i][j]==2:
                count[i][j] += 1

    for i in range(grid_size):
        for j in range(grid_size):
            c = count[i][j]
            if c==1:
                new_grid[i][j] = 1
            if c>=2:
                k = random.random()
                if k>=0.7:
                    for a in lst:
                        new_grid[(i+a[0])%grid_size][(j+a[1])%grid_size] = 2

    return new_grid

# Generate unique colors for each possible cell value
random_colors = []
for i in range(3):  # Assuming 3 possible cell values: 0, 1, and 2
    random_colors.append(np.random.rand(1, 3))

# Update the random_colors list to include the newly generated colors
random_colors = np.vstack(random_colors)

# Create a custom colormap
custom_cmap = ListedColormap(random_colors)

# Plot setup
fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', on_click)
ax.axis('off')

# custom_cmap = ListedColormap(['black', 'red', 'white'])

start_time = time.time()
time_limit = 45  # Time limit in seconds

t = []
n = []

while True:
    if time.time() - start_time > time_limit:
        print("Time limit reached. Exiting...")
        break
    if not paused:
        ax.clear()
        rgb_grid = np.zeros((grid_size, grid_size, 3))

        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == 1:
                    rgb_grid[i][j] = np.random.rand(3)  # Random color for each '1'
                elif grid[i][j] == 2:
                    rgb_grid[i][j] = [1.0, 1.0, 1.0]  # White for '2'
                else:
                    rgb_grid[i][j] = [0.0, 0.0, 0.0]  # Black for '0'

        ax.imshow(rgb_grid, interpolation='nearest')
        ax.axis('off')
        t.append(time.time() - start_time)
        n.append(np.sum(grid > 0))
        plt.pause(0.05)  # Refresh every 0.1 seconds
        grid = update_grid3(grid)
    else:
        plt.close()
        break

plt.close()
plt.cla()
plt.clf()
plt.plot(t, n)
plt.show()
