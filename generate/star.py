import numpy as np


class GenStar:
    def conv(self, array, size, stride):
        array = np.pad(array, 2, 'constant', constant_values=0)
        array_star = np.zeros(np.shape(array))

        for cy in range(0, np.shape(array)[0], stride):
            for cx in range(0, np.shape(array)[1], stride):
                convsum = np.sum(array[cy:cy + size[1], cx:cx + size[0]])
                print(cx, convsum)

                if convsum > 10:
                    array_star[cy][cx] = 0.5
                else:
                    array_star[cy][cx] = 0

            print('=' * 25, cy, '=' * 25)

        return array_star
