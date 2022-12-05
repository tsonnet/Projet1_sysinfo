from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys

from Extract_data import Extract_data,Extract_data_boxplot

def plot_continue(path1, path2, path3,case):

    X1, Y1 = Extract_data(path1,5)

    X2,Y2 = Extract_data(path2,5)

    X3,Y3 = Extract_data(path3,5)

    fig = plt.figure(figsize = (5, 10))
    ax1 = fig.add_subplot(3,1,1)
    ax2 = fig.add_subplot(3,1,2)
    ax3 = fig.add_subplot(3,1,3)

    ax1.plot(X1,Y1,'-b')
    ax1.set_xlabel('Number of threads')
    ax1.set_ylabel('Time in milliseconds')
    ax1.set_title('Philosophes')

    ax2.plot(X2,Y2,'-g')
    ax2.set_xlabel('Number of threads')
    ax2.set_ylabel('Time in milliseconds')
    ax2.set_title('Lececriv')

    ax3.plot(X3,Y3,'-r')
    ax3.set_xlabel('Number of threads')
    ax3.set_ylabel('Time in milliseconds')
    ax3.set_title('Prodcons')
    fig.tight_layout()

    if(case == 'ordi'):
        plt.savefig('graph_.png')
    else:
        plt.savefig('graph_inginious.png')

    plt.show(block = False)


def individual_plot_continue(path1, path2, path3,case):

    X1, Y1 = Extract_data(path1,5)

    X2,Y2 = Extract_data(path2,5)

    X3,Y3 = Extract_data(path3,5)

    plt.figure()
    plt.plot(X1,Y1,'-b')
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Philisophes')
    if (case == 'ordi'):
        plt.savefig("philosophes.png")
    else:
        plt.savefig("philosophes_inginious.png")
        
    plt.figure()
    plt.plot(X2,Y2,'-g')
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Lececriv')
    if case == 'ordi':
        plt.savefig("lececriv.png")
    
    else :
        plt.savefig("lececriv_inginious.png")

    plt.figure()
    plt.plot(X3,Y3,'-r')
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Prodcons')
    if (case == 'ordi'):
        plt.savefig("prodcons.png")
    else :
    	plt.savefig("prodcons_inginious.png")

X1_plot, Y1_plot = Extract_data_boxplot('Part1/Timer/philosophes.csv',5)

X2_plot,Y2_plot = Extract_data_boxplot('Part1/Timer/lececriv.csv',5)

X3_plot,Y3_plot = Extract_data_boxplot('Part1/Timer/prodcons.csv',5)

def plot_boxplot(path1, path2, path3,case):

    X1_plot, Y1_plot = Extract_data_boxplot(path1,5)

    X2_plot,Y2_plot = Extract_data_boxplot(path2,5)

    X3_plot,Y3_plot = Extract_data_boxplot(path3,5)

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
    if (case == 'ordi'):
        plt.savefig('graph_boxplot.png')
    else :
        plt.savefig('graph_boxplot_inginious.png')
    plt.show(block = False)

def individual_plot_boxplot(path1, path2, path3,case):

    X1_plot, Y1_plot = Extract_data_boxplot(path1,5)

    X2_plot,Y2_plot = Extract_data_boxplot(path2,5)

    X3_plot,Y3_plot = Extract_data_boxplot(path3,5)

    plt.figure()
    plt.boxplot(Y1_plot)
    plt.gca().get_xaxis().set_ticklabels(X1_plot)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Philosophes')
    if (case == 'ordi'):
        plt.savefig("philosophes_boxplot.png")
    else :
        plt.savefig("philosophes_boxplot_inginious.png")

    plt.figure()
    plt.boxplot(Y2_plot)
    plt.gca().get_xaxis().set_ticklabels(X2_plot)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Lececriv')
    if (case == 'ordi'):
        plt.savefig("lececriv_boxplot.png") 
    else :
        plt.savefig("lececriv_boxplot_inginious.png")

    plt.figure()
    plt.boxplot(Y3_plot)
    plt.gca().get_xaxis().set_ticklabels(X3_plot)
    plt.xlabel('Number of threads')
    plt.ylabel('Time in milliseconds')
    plt.title('Prodcons')
    if (case == 'ordi'):
        plt.savefig("prodcons_boxplot.png")
    else :
    	plt.savefig("prodcons_boxplot_inginious.png")
    	
if len( sys.argv ) <= 2:
    print('Besoin de 2 paramètres')
    exit()

if len(sys.argv) > 7:
    print("Trop d'arguments")
    exit()
try:
        param = str(sys.argv[1])
except ValueError: 
        print( "Bad parameter value: %s" % sys.argv, file=sys.stderr )  

if(str(sys.argv[1]) == "continue" and str(sys.argv[2]) == 'subplot'):
    plot_continue(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
elif(str(sys.argv[1]) == "continue" and str(sys.argv[2]) == 'plot'):
    individual_plot_continue(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
elif(str(sys.argv[1]) == "boxplot" and str(sys.argv[2]) == 'subplot'):
    plot_boxplot(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
elif(str(sys.argv[1]) == "boxplot" and str(sys.argv[2]) == 'plot'):
    individual_plot_boxplot(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
else :
    print("Argument non-défini")
