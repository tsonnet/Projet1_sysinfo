from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def Extract_data(path,nb_rep):

    data = pd.read_csv(path)

    X = data[data.columns.values[0]]
    Y = data[data.columns.values[2]]

    print(X)
    print(Y)

    List_average = []

    for i in range(int(len(Y)/nb_rep)):
        sum = 0
        for j in range(nb_rep):
            datetime_str = Y[i*5 + j]
            datetime_object = datetime.strptime(datetime_str, "%M:%S.%f")
            total_milisecond = int(datetime_object.microsecond/1000)
            sum += total_milisecond
        List_average.append(sum/nb_rep)


    average = np.average(List_average)
    standard_deviation = np.std(List_average)
    
    x = X[::nb_rep]
    
    return x,List_average