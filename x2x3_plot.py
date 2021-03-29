import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print('Starting ...')
    
    x0, x1 = np.meshgrid(np.linspace(-5,5,100), np.linspace(-5,5,100))
    y=x0 ** 2 + x1 ** 3
    print(x0)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x0, x1, y)
    plt.show()
