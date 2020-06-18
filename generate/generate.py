import numpy as np
import matplotlib.pyplot as plt

import generate.perlin as perlin


class SpaceGenerator:
    def __init__(self):
        lin = np.linspace(0, 5, 1000, endpoint=False)
        x, y = np.meshgrid(lin, lin)  # FIX3: I thought I had to invert x and y here but it was a mistake

        plt.imshow(perlin.perlin(x, y, seed=123), origin='upper')
        plt.show()
