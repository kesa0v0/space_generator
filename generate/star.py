import numpy as np


class GenStar:
    def conv(self, array, size, stride):
        array = np.pad(array, 2, 'constant', constant_values=0)
        array_star = np.zeros(np.shape(array))

        for cy in range(stride, np.shape(array)[0] - stride, stride):
            for cx in range(stride, np.shape(array)[1] - stride, stride):
                convsum = np.sum(array[cy:cy + size[1], cx:cx + size[0]])
                print(cx, convsum)

                if convsum > 15:
                    array_star[cy+np.random.randint(0, 5)][cx+np.random.randint(0, 5)] = np.random.randint(1, 8)
                elif convsum > 10:
                    array_star[cy + np.random.randint(0, 5)][cx + np.random.randint(0, 5)] = np.random.randint(1, 6)
                elif convsum > 5:
                    array_star[cy + np.random.randint(0, 5)][cx + np.random.randint(0, 5)] = np.random.randint(1, 4)
                else:
                    array_star[cy + np.random.randint(0, 5)][cx + np.random.randint(0, 5)] = np.random.randint(1, 2)

            print('=' * 25, cy, '=' * 25)

        return array_star
