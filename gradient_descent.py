import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def g_2x(x):
    return 2*x

def MSE(x, y, theta):
    m = y.shape[0]
    cost = (1 / (2 * m)) * np.sum((theta * x - y) ** 2)
    return cost

def MSE_derivative(x, y, theta):
    m = y.shape[0]
    cost_derivative = (1 / m) * np.sum((theta * x - y) * x)
    return cost_derivative



if __name__ == "__main__":
    print('Starting ...')

    data = pd.read_csv("./power_rpm.csv", sep=";")
    #print(data.iloc[:100])
    
    X = data['ME_Power'].to_numpy().reshape(-1, 1)
    Y = data['ME_RPM'].to_numpy().reshape(-1, 1)
    
    standard_scaler = StandardScaler()
    X = standard_scaler.fit_transform(X)
    Y = standard_scaler.fit_transform(Y)
    print('@0 = ', MSE_derivative(x=X, y=Y,theta=0))

    lr = 0.01
    theta = 0
    theta_all = []
    cost_all = []

    for i in range(300):
        theta = theta - lr * MSE_derivative(x=X, y=Y,theta=0)
        cost = MSE(X, Y, theta)
        theta_all.append(theta)
        cost_all.append(cost)

    #print('min = ', min(theta_all))
    best_slope = min(theta_all)
    print('min = ', best_slope)

    x_axis = np.arange(-4, 4, 0.1)
    y_axis = best_slope * x_axis


    #plt.scatter(theta_all, cost_all, linewidth=1.5, c=np.arange(len(cost_all)))
    #plt.scatter(data['ME_Power'], data['ME_RPM'], alpha=0.9)
    plt.scatter(X, Y, alpha=0.4, zorder=0)
    plt.plot(x_axis, y_axis, c='#FF8177')
    plt.show()