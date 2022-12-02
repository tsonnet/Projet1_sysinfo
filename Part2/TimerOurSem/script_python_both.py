from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

from Projet1_sysinfo.Part1.Timer.Extract_data import Extract_data

    
X1, Y1 = Extract_data('PhilosophesOurSem.csv',5)
X1bis, Y1bis = Extract_data('philosophes.csv',5)

X2,Y2 = Extract_data('LececrivOurSem.csv',5)
X2bis,Y2bis = Extract_data('lececriv.csv',5)

X3,Y3 = Extract_data('ProdconsOurSEm.csv',5)
X3bis,Y3bis = Extract_data('Prodcons.csv',5)

fig, axes = plt.subplots(3, 1)
ax1, ax2,ax3 = axes

ax1.plot(X1,Y1,'-b')
ax1.plot(X1bis,Y1bis,'-r')
ax1.xlabel('Number of threads')
ax1.ylabel('Time in milliseconds')
ax1.title('PhilisophesOurSem vs Philosophes')

ax2.plot(X2,Y2,'-b')
ax2.plot(X2bis,Y2bis,'-r')
ax2.xlabel('Number of threads')
ax2.ylabel('Time in milliseconds')
ax2.title('LececrivOurSem vs Lececriv')

ax3.plot(X3,Y3,'-b')
ax3.plot(X3bis,Y3bis,'-r')
ax1.xlabel('Number of threads')
ax1.ylabel('Time in milliseconds')
ax1.title('ProdconsOurSem vs Prodcons')

fig.tight_layout()
plt.show()