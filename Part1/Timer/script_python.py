from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys

from Extract_data import Extract_data,Extract_data_boxplot

def plot_continue():  
    X1, Y1 = Extract_data('philosophes.csv',5)

    X2,Y2 = Extract_data('lececriv.csv',5)

    X3,Y3 = Extract_data('prodcons.csv',5)

    fig = plt.figure(figsize = (5, 10))
    ax1 = fig.add_subplot(3,1,1)
    ax2 = fig.add_subplot(3,1,2)
    ax3 = fig.add_subplot(3,1,3)

    ax1.plot(X1,Y1,'-b')
    ax1.set_xlabel('Number of threads')
    ax1.set_ylabel('Time in milliseconds')
    ax1.set_title('Philisophes')

    ax2.plot(X2,Y2,'-g')
    ax2.set_xlabel('Number of threads')
    ax2.set_ylabel('Time in milliseconds')
    ax2.set_title('Lececriv')

    ax3.plot(X3,Y3,'-r')
    ax3.set_xlabel('Number of threads')
    ax3.set_ylabel('Time in milliseconds')
    ax3.set_title('Prodcons')

    fig.tight_layout()
    plt.savefig('graph.png')
    plt.show(block = False)

def plot_boxplot():
    X1, Y1 = Extract_data_boxplot('philosophes.csv',5)

    X2,Y2 = Extract_data_boxplot('lececriv.csv',5)

    X3,Y3 = Extract_data_boxplot('prodcons.csv',5)

    fig = plt.figure(figsize = (5, 10))
    ax1 = fig.add_subplot(3,1,1)
    ax2 = fig.add_subplot(3,1,2)
    ax3 = fig.add_subplot(3,1,3)

    ax1.boxplot(Y1)
    ax1.xaxis.set_ticklabels(X1)
    ax1.set_xlabel('Number of threads')
    ax1.set_ylabel('Time in milliseconds')
    ax1.set_title('Philisophes')

    ax2.boxplot(Y2)
    ax2.xaxis.set_ticklabels(X2)
    ax2.set_xlabel('Number of threads')
    ax2.set_ylabel('Time in milliseconds')
    ax2.set_title('Lececriv')

    ax3.boxplot(Y3)
    ax3.xaxis.set_ticklabels(X3)
    ax3.set_xlabel('Number of threads')
    ax3.set_ylabel('Time in milliseconds')
    ax3.set_title('Prodcons')

    fig.tight_layout()
    plt.savefig('graph_boxplot.png')
    plt.show(block = False)


if len( sys.argv ) == 1:
    print('Besoin de paramètres gros con')
    exit()

if len(sys.argv) > 2:
    print("Trop d'arguments")
    exit()
try:
        param = str(sys.argv[1])
except ValueError: 
        print( "Bad parameter value: %s" % sys.argv, file=sys.stderr )  

if(str(sys.argv[1]) == "continue"):
    plot_continue()
elif(str(sys.argv[1]) == "boxplot"):
    plot_boxplot()
else :
    print("Argument non-défini")