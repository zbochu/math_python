import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print('Starting ...')

 #   data = pd.read_csv("https://raw.githubusercontent.com/hadrienj/essential_math_for_data_science/master/data/beer_dataset.csv", sep=",")
 #   data = pd.read_csv("https://raw.githubusercontent.com/hadrienj/essential_math_for_data_science/master/data/happiness_2020.csv", sep=",")
    data = pd.read_csv("./power_rpm.csv", sep=";")

    
 #   print(data)
   
 #   X = data['Temperatura Maxima (C)']
 #   Y = data['Consumo de cerveja (litros)']

 #   X = data['Perceptions of corruption']
 #   Y = data['Ladder score']

    X = data['ME_Power']
    Y = data['ME_RPM']

    cov = np.sum((X - X.mean()) * (Y - Y.mean())) / X.shape[0]
    print('Covariance(calc) = ', cov)
    print('Covariance(numpy) = ', np.cov(X, Y))
    print('Correlation =', np.corrcoef(X, Y))

    plt.scatter(X, Y, alpha=0.5)
    plt.show()