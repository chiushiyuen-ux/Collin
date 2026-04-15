import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x), color='blue')

# Set the limits and labels
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sine Wave Animation')

# Define different arrays to animate
arrays = [np.sin(x), np.sin(2 * x), np.sin(3 * x), np.sin(4 * x), np.sin(5 * x)]

# Animation function
def update(frame):
    line.set_ydata(arrays[frame])  # Update the data of the line
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(arrays), interval=500, blit=True)

# Show the animation
plt.show()