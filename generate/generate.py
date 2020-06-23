import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

import generate.perlin as perlin
import generate.star as star


def normalization(a, size=1):
    return size * (a - np.min(a)) / np.ptp(a)


class SpaceGenerator:
    def __init__(self):
        lin = np.linspace(0, 5, 500, endpoint=False)
        x, y = np.meshgrid(lin, lin)

        pl = perlin.perlin(x, y, seed=1230)[:250]
        pl = normalization(pl)

        print(np.shape(pl), np.max(pl), np.min(pl))
        gen_star = star.GenStar()
        map_star = gen_star.conv(pl, (5, 5), 5)

        plt.imshow(map_star, origin='upper')
        plt.colorbar()
        plt.show()


