from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

from Projet1_sysinfo.Part1.Timer.Extract_data import Extract_data,Extract_data_boxplot

    
X1, Y1 = Extract_data('PhilosophesOurSem.csv',5)
X1bis, Y1bis = Extract_data('philosophes.csv',5)

X2,Y2 = Extract_data('LececrivOurSem.csv',5)
X2bis,Y2bis = Extract_data('lececriv.csv',5)

X3,Y3 = Extract_data('ProdconsOurSEm.csv',5)
X3bis,Y3bis = Extract_data('Prodcons.csv',5)

fig = plt.figure(figsize = (5, 10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.plot(X1,Y1,'-b')
ax1.plot(X1bis,Y1bis,'-r')
ax1.set_xlabel('Number of threads')
ax1.set_ylabel('Time in milliseconds')
ax1.set_title('PhilisophesOurSem vs Philosophes')

ax2.plot(X2,Y2,'-b')
ax2.plot(X2bis,Y2bis,'-r')
ax2.set_xlabel('Number of threads')
ax2.set_ylabel('Time in milliseconds')
ax2.set_title('LececrivOurSem vs Lececriv')

ax3.plot(X3,Y3,'-b')
ax3.plot(X3bis,Y3bis,'-r')
ax3.set_xlabel('Number of threads')
ax3.set_ylabel('Time in milliseconds')
ax3.set_title('ProdconsOurSem vs Prodcons')

fig.tight_layout()
plt.savefig('graph.png')
plt.show(block = False)

from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys

from Part1.Timer.Extract_data import Extract_data,Extract_data_boxplot

X1, Y1 = Extract_data('Part1/Timer/philosophesOurSem.csv',5)
X1bis, Y1bis = Extract_data('philosophes.csv',5)

X2,Y2 = Extract_data('Part1/Timer/lececrivOurSem.csv',5)
X2bis,Y2bis = Extract_data('lececriv.csv',5)

X3,Y3 = Extract_data('Part1/Timer/prodconsOurSem.csv',5)
X3bis,Y3bis = Extract_data('Prodcons.csv',5)

def plot_continue():  

    fig = plt.figure(figsize = (5, 10))
    ax1 = fig.add_subplot(3,1,1)
    ax2 = fig.add_subplot(3,1,2)
    ax3 = fig.add_subplot(3,1,3)

    ax1.plot(X1,Y1,'-b')
    ax1.plot(X1bis,Y1bis,'-r')
    ax1.set_xlabel('Number of threads')
    ax1.set_ylabel('Time in milliseconds')
    ax1.set_title('Philisophes')

    ax2.plot(X2,Y2,'-b')
    ax2.plot(X2bis,Y2bis,'-r')
    ax2.set_xlabel('Number of threads')
    ax2.set_ylabel('Time in milliseconds')
    ax2.set_title('Lececriv')

    ax3.plot(X3,Y3,'-b')
    ax3.plot(X3bis,Y3bis,'-r')          
    ax3.set_xlabel('Number of threads')
    ax3.set_ylabel('Time in milliseconds')
    ax3.set_title('Prodcons')

    fig.tight_layout()
    plt.savefig('graph.png')
    plt.show(block = False)


def individual_plot_continue():

    plt.figure()
    plt.plot(X1,Y1,'-b')
    plt.plot(X1bis,Y1bis,'-r')
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Philisophes')
    plt.savefig("philisophes.png")

    plt.figure()
    plt.plot(X2,Y2,'-b')
    plt.plot(X2bis,Y2bis,'-r')
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Lececriv')
    plt.savefig("lececriv.png")

    plt.figure()
    plt.plot(X3,Y3,'-b')
    plt.plot(X3bis,Y3bis,'-r')
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Prodcons')
    plt.savefig("prodcons.png")

X1_plot, Y1_plot = Extract_data_boxplot('Part2/Timer/philosophesOurSem.csv',5)

X2_plot,Y2_plot = Extract_data_boxplot('Part2/Timer/lececrivOurSem.csv',5)

X3_plot,Y3_plot = Extract_data_boxplot('Part2/Timer/prodconsOurSem.csv',5)

def plot_boxplot():

    fig = plt.figure(figsize = (5, 10))
    ax1 = fig.add_subplot(3,1,1)
    ax2 = fig.add_subplot(3,1,2)
    ax3 = fig.add_subplot(3,1,3)

    ax1.boxplot(Y1_plot)
    ax1.xaxis.set_ticklabels(X1_plot)
    ax1.set_xlabel('Number of threads')
    ax1.set_ylabel('Time in milliseconds')
    ax1.set_title('Philisophes')

    ax2.boxplot(Y2_plot)
    ax2.xaxis.set_ticklabels(X2_plot)
    ax2.set_xlabel('Number of threads')
    ax2.set_ylabel('Time in milliseconds')
    ax2.set_title('Lececriv')

    ax3.boxplot(Y3_plot)
    ax3.xaxis.set_ticklabels(X3_plot)
    ax3.set_xlabel('Number of threads')
    ax3.set_ylabel('Time in milliseconds')
    ax3.set_title('Prodcons')

    fig.tight_layout()
    plt.savefig('graph_boxplot.png')
    plt.show(block = False)

def individual_plot_boxplot():

    plt.figure()
    plt.boxplot(Y1_plot)
    plt.gca().get_xaxis().set_ticklabels(X1_plot)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Philosophes')
    plt.savefig("philosophes_boxplot.png")

    plt.figure()
    plt.boxplot(Y2_plot)
    plt.gca().get_xaxis().set_ticklabels(X2_plot)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Lececriv')
    plt.savefig("lececriv_boxplot.png")

    plt.figure()
    plt.boxplot(Y3_plot)
    plt.gca().get_xaxis().set_ticklabels(X3_plot)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Prodcons')
    plt.savefig("prodcons_boxplot.png")

if len( sys.argv ) <= 2:
    print('Besoin de 2 paramètres')
    exit()

if len(sys.argv) > 3:
    print("Trop d'arguments")
    exit()
try:
        param = str(sys.argv[1])
except ValueError: 
        print( "Bad parameter value: %s" % sys.argv, file=sys.stderr )  

if(str(sys.argv[1]) == "continue" and str(sys.argv[2]) == 'subplot'):
    plot_continue()
elif(str(sys.argv[1]) == "continue" and str(sys.argv[2]) == 'plot'):
    individual_plot_continue()
elif(str(sys.argv[1]) == "boxplot" and str(sys.argv[2]) == 'subplot'):
    plot_boxplot()
elif(str(sys.argv[1]) == "boxplot" and str(sys.argv[2]) == 'plot'):
    individual_plot_boxplot()
else :
    print("Argument non-défini")