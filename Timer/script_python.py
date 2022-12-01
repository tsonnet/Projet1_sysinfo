import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(List[::5])

""" def little_plot(path,title,fx1,fx2):

    data = pd.read_csv(path)

    X = data[data.columns.values[0]]
    Y = data[data.columns.values[1]]

    moyennes = X[::5]/5

    
    data = list(data['Windspeed'])
    x = np.linspace(min(data), max(data))
    
    plt.plot(x, fx1, '-g', label = "InvGauss")
    plt.plot(x, fx2, '-r', label = "Gamma")
    
    plt.hist(data, bins=30, range=(0,130), density = 1)
    plt.title(title +" winspeed histogram")
    plt.xlabel("Windspeed [km/h]")
    plt.legend()
    plt.show()
    
    return """