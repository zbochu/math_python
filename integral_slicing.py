import numpy as np
import matplotlib.pyplot as plt

def g_2x(x):
    return 2*x


if __name__ == "__main__":
    print('Starting ...')
    delta_x = 0.5
    x = np.arange(0,7,delta_x)
    y = g_2x(x)

    slice_area_all = np.zeros(y.shape[0])
    for i in range(1, len(x)):
        slice_area_all[i] = delta_x * y[i-1]

    slice_area_all = slice_area_all.cumsum()

    plt.plot(x, x**2, label='True')
    plt.plot(x, slice_area_all, label='Estimated')
    plt.show()
