import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import random


# Grid size
grid_size = 25
grid = np.zeros((grid_size, grid_size))
siz = 5
pts = []
for m in range(-(siz),siz+1):
    for n in range(-(siz),siz+1):
        if m**2+n**2 <= siz**2:
            pts.append((m,n))
pts.remove((0,0))

click_count = 0  # Initialize click counter

def color1(i, j):
    ptschosen = []
    p = 0.3
    for pt in pts:
        r = random.random()
        if 0.5-p/2<r<=0.5+p/2:
            ptschosen.append(pt)
    grid[i][j] = 1
    for pt in ptschosen:
        grid[(i+pt[0])%grid_size][(j+pt[1])%grid_size] = 1

def color2(i,j):
    ptschosen = random.sample(pts, 12)
    grid[i][j] = 1
    for pt in ptschosen:
        grid[(i+pt[0])%grid_size][(j+pt[1])%grid_size] = 1


def is_grid_full():
    return np.sum(grid) >= 0.5 * grid_size ** 2

# Function to handle clicks
def onclick(event):
    global click_count
    if event.inaxes is not None:
        i, j = int(event.ydata), int(event.xdata)
        color1(i,j)
        #grid[i, j] = 1
        click_count += 1
        ax.clear()
        ax.imshow(grid, cmap='gray', interpolation='nearest')
        ax.axis('off')
        fig.canvas.draw()
        
        if is_grid_full():
            print(f"Grid half colored! Number of clicks: {click_count}")
            fig.canvas.mpl_disconnect(cid)  # Disconnect the click event
            plt.close(fig)  # Close the figure

# Plot setup
fig, ax = plt.subplots()
cid = fig.canvas.mpl_connect('button_press_event', onclick)
ax.imshow(grid, cmap='gray', interpolation='nearest')
ax.axis('off')
plt.show()
