from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys

from Extract_data import Extract_data,Extract_data_boxplot

def plot_continue(path1, path2, path3,case):

    X1, Y1, Var1 = Extract_data(path1,5)

    X2,Y2, Var2 = Extract_data(path2,5)

    X3,Y3, Var3 = Extract_data(path3,5)

    fig = plt.figure(figsize = (5, 10))
    ax1 = fig.add_subplot(3,1,1)
    ax2 = fig.add_subplot(3,1,2)
    ax3 = fig.add_subplot(3,1,3)

    ax1.plot(X1,Y1,'-b')
    ax1.errorbar(X1, Y1, yerr = Var1)
    ax1.set_xlabel('Number of threads')
    ax1.set_ylabel('Time in milliseconds')
    if "2" in path1:
        ax1.set_title('PhilosophesOurSem')
    else:
        ax1.set_title('Philosophes')

    ax2.plot(X2,Y2)
    ax2.errorbar(X2, Y2, yerr = Var2)
    ax2.set_xlabel('Number of threads')
    ax2.set_ylabel('Time in milliseconds')
    if "2" in path2 :
        ax2.set_title('LececrivOurSem')
    else :
        ax2.set_title('Lececriv')

    ax3.plot(X3,Y3)
    ax3.errorbar(X3, Y3, yerr = Var3)
    ax3.set_xlabel('Number of threads')
    ax3.set_ylabel('Time in milliseconds')
    if "2" in path3 :
        ax3.set_title('ProdconsOurSem')
    else:
        ax3.set_title('Prodcons')
    	
    fig.tight_layout()

    if(case == 'ordi'):
        plt.savefig('graph_.png')
    else:
        plt.savefig('graph_inginious.png')

    plt.show(block = False)


def twoplot(path1,path2,title):

    X1, Y1,Var1 = Extract_data(path1,5)

    X2,Y2,Var2 = Extract_data(path2,5)

    plt.figure()
    plt.plot(X1,Y1,'-r')
    plt.plot(X2,Y2,'-g')
    plt.errorbar(X1, Y1, yerr = np.array(Var1,dtype='float64')*0.2, color= 'red')
    plt.errorbar(X2, Y2, yerr = np.array(Var2,dtype='float64')*0.2, color= 'green')
    plt.ylim(0, max(Y1+Y2)+10)
    plt.xlabel('Number of threads')
    plt.ylabel('Execution time in milliseconds')
    plt.title('Evolution of execution time vs number of threads')
    plt.legend(['TestAndSet','TestAndTestAndSet'])
    plt.grid()
    plt.savefig(title)
    plt.show(block = False)

def treeplot(path1,path2,path3,title):

    X1, Y1,Var1 = Extract_data(path1,5)

    X2,Y2,Var2 = Extract_data(path2,5)

    X3,Y3,Var3 = Extract_data(path3,5)

    plt.figure()
    plt.plot(X1,Y1,'-r')
    plt.plot(X2,Y2,'-g')
    plt.plot(X3,Y3,'-y')
    plt.errorbar(X1, Y1, yerr = np.array(Var1,dtype='float64')*0.2, color= 'red')
    plt.errorbar(X2, Y2, yerr = np.array(Var2,dtype='float64')*0.2, color= 'green')
    plt.errorbar(X3, Y3, yerr = np.array(Var2,dtype='float64')*0.2, color= 'yellow')
    plt.ylim(0, max(Y1+Y2)+10)
    plt.xlabel('Number of threads')
    plt.ylabel('Execution time [ms]')
    plt.title('Evolution of execution time vs number of threads')
    plt.legend(['TestAndSet','TestAndTestAndSet','POSIX'])
    plt.grid()
    plt.savefig(title)
    plt.show(block = False)


    	
if len( sys.argv ) <= 2:
    print('Besoin de 2 paramètres')
    exit()

try:
        param = str(sys.argv[1])
except ValueError: 
        print( "Bad parameter value: %s" % sys.argv, file=sys.stderr )  

if(str(sys.argv[1]) == 'subplot'):
    plot_continue(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
elif (str(sys.argv[1]) == "plot2"):
    twoplot(sys.argv[2],sys.argv[3],sys.argv[4])
elif(str(sys.argv[1]) == "plot3"):
    treeplot(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
else :
    print("Argument non-défini")
