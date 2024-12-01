import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# CONSTANTS
# mu-z-over-four-pi
mzofp = 1e-7
# charge of electron
qe = 1.6e-19
# mass of proton
mproton = 1.7e-27
# initial velocity
v0 = 2e6
# B strength (T)
B = 0.2

# time parameters
# simulation time
t_max = 10 
# time step
dt = 0.02
t = np.arange(0, t_max, dt)


def setup(ax):
    # Create a figure and axis
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # axes background
    x_ticks = np.arange(-5, 6, 1)
    y_ticks = np.arange(-5, 6, 1)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.grid(True, which='both', linestyle='--', color='gray', alpha=0.5)

    # Add labels and title
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_title("Uniform Magnetic Field Simulation (Out of the Page)")

def B_field(marker, size):
    # B field mesh grid
    x, y = np.meshgrid(np.arange(-5, 6, 1), np.arange(-5, 6, 1))
    ax.scatter(x, y, color='black', s=size, marker=marker)


if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(6, 6))

    # figure and axis
    setup(ax)

    # if B is negative, x
    if B < 0:
        B_field('x', 20)
    # if B is positive, o
    else:
        B_field('o', 3)
    
    # r = mproton * v0 / q * B




    plt.show()