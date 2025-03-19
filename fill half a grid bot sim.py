import numpy as np
import random
import matplotlib.pyplot as plt

# Grid settings
grid_size = 25
siz = 5
runs = 40

# Generate the neighborhood points
pts = []
for m in range(-siz, siz + 1):
    for n in range(-siz, siz + 1):
        if m**2 + n**2 <= siz**2:
            pts.append((m, n))
pts.remove((0, 0))

def color1(grid, i, j, p):
    ptschosen = []
    for pt in pts:
        r = random.random()
        if 0.5 - p / 2 < r <= 0.5 + p / 2:
            ptschosen.append(pt)
    grid[i][j] = 1
    for pt in ptschosen:
        grid[(i + pt[0]) % grid_size][(j + pt[1]) % grid_size] = 1

def is_grid_half_full(grid):
    return np.sum(grid) >= 0.5 * grid_size ** 2

def bot(p):
    # Run simulations
    click_counts = []

    for _ in range(runs):
        grid = np.zeros((grid_size, grid_size))
        click_count = 0
        while not is_grid_half_full(grid):
            i, j = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            if (grid[i, j] == 0) or True:  # Only click empty squares
                color1(grid, i, j, p)
                click_count += 1
        click_counts.append(click_count)

        # Plot each grid
        #plt.imshow(grid, cmap='gray', interpolation='nearest')
        #plt.axis('off')
        #plt.show()

    return click_counts

# Display results
#print("Clicks per run:", click_counts)
#print("Average clicks:", np.mean(click_counts))

x = []
y = []
for i in range(1,21):
    x.append(i*0.05)
    y.append(np.mean(bot(i*0.05)))


plt.scatter(x,y)
plt.show()

