import numpy as np
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print('Starting ...')
    rolls = np.random.randint(1, 7, 100)
    print(rolls)

    val, counts = np.unique(rolls, return_counts=True)
    plt.stem(val, counts/len(rolls), basefmt="C2-", use_line_collection=True)

    plt.show()