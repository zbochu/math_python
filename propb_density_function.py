import numpy as np
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print('Starting ...')
    np.random.seed(123)
    data = np.random.normal(0.3, 0.1, 1000)
    print(data)

    hist = plt.hist(data, bins=24, range=(-0.2, 1), density=True)

    plt.show()