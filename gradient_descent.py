import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg

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

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

if __name__ == "__main__":
    print('Starting ...')
    matplotlib.use("TkAgg")

#    data = pd.read_csv("./power_rpm.csv", sep=";")
    data = pd.read_csv("./aer.csv", sep=",")
#    data = pd.read_csv("https://raw.githubusercontent.com/hadrienj/essential_math_for_data_science/master/data/beer_dataset.csv", sep=",")
#    data = pd.read_csv("https://raw.githubusercontent.com/hadrienj/essential_math_for_data_science/master/data/happiness_2020.csv", sep=",")
    

#    print(data.iloc[:100])
#    X = data['Temperatura Maxima (C)'].to_numpy().reshape(-1, 1)
#    Y = data['Consumo de cerveja (litros)'].to_numpy().reshape(-1, 1)

#    X = data['ME_Power'].to_numpy().reshape(-1, 1)
#    Y = data['ME_RPM'].to_numpy().reshape(-1, 1)

    X = data['Time'].to_numpy().reshape(-1, 1)
    Y = data['AER'].to_numpy().reshape(-1, 1)
    Z = data['PI'].to_numpy().reshape(-1, 1)


#    X = data['Perceptions of corruption'].to_numpy().reshape(-1, 1)
#    Y = data['Ladder score'].to_numpy().reshape(-1, 1)

    
    standard_scaler = StandardScaler()
    X = standard_scaler.fit_transform(X)
    Y = standard_scaler.fit_transform(Y)
    Z = standard_scaler.fit_transform(Z)
    print('@0 = ', MSE_derivative(x=X, y=Y,theta=0))

    lr = 0.01
    theta = 0
    theta_all = []
    cost_all = []
    costF = np.empty((0,2), dtype=np.float64)

    for i in range(300):
        theta = theta - lr * MSE_derivative(x=X, y=Y,theta=0)
        cost = MSE(X, Y, theta)
        theta_all.append(theta)
        cost_all.append(cost)
        costF =  np.concatenate((costF, [[theta, cost]]), axis = 0)

    #print(theta_all)
    # theta_all, cost_all = costF[:, :-1], costF[:, -1]
    #print('Minimum Theta = ', costF[np.argmin(cost_all), 0])
    #min_index = np.unravel_index(np.argmin(costF, axis=0), costF.shape)
    
    #best_slope = costF[np.argmin(cost_all), 0]
    min_i = np.argmin(cost_all)
    print('min index = ', min_i)
    best_slope = theta_all[min_i]
    print('min = ', best_slope)

    x_axis = np.arange(-4, 4, 0.1)
    y_axis = best_slope * x_axis

    #plt.scatter(theta_all, cost_all, linewidth=1.5, c=np.arange(len(cost_all)))
    #plt.scatter(theta_all, cost_all, linewidth=1.5, c=np.arange(len(cost_all)))
    #plt.scatter(data['ME_Power'], data['ME_RPM'], alpha=0.9)
    plt.scatter(X, Y, alpha=.5, zorder=0)
    plt.scatter(X, Z, alpha=.5, zorder=0)
    plt.plot(x_axis, y_axis, c='#FF8177')
    plt.show()