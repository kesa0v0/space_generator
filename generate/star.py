import numpy as np


class GenStar:
    def conv(self, array, size, stride):
        array = np.pad(array, 2, 'constant', constant_values=0)
        array_star = np.zeros(np.shape(array))

        for cy in range(0, np.shape(array)[0], stride):
            for cx in range(0, np.shape(array)[1], stride):
                convsum = np.sum(array[cy:cy + size[1], cx:cx + size[0]])
                print(convsum)

        return ""