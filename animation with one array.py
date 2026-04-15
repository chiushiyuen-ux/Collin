import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
L = 100  # Size of matrix
t_values = np.linspace(0, 2 * np.pi, 100)  # Time values
x = np.linspace(-5, 5, L)  # X values

# Initialize the matrix
def calculate_matrix(t):
    return np.sin(x[:, np.newaxis] + t)  # Example function (can be modified)

# Create the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], color='blue')
ax.set_xlim(-5, 5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Animation of Transforming (x, y) with Time t')

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function for animation
def update(frame):
    t = t_values[frame]
    y = calculate_matrix(t)
    line.set_data(x, y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(t_values), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()