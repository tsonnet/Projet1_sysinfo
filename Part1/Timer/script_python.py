from datetime import date
from tarfile import LENGTH_LINK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

from Projet1_sysinfo.Part1.Timer.Extract_data import Extract_data

    
X1, Y1 = Extract_data('philosophes.csv',5)

X2,Y2 = Extract_data('lececriv.csv',5)

X3,Y3 = Extract_data('Prodcons.csv',5)

fig, axes = plt.subplots(3, 1)
ax1, ax2,ax3 = axes

ax1.plot(X1,Y1,'-b')
ax1.xlabel('Number of threads')
ax1.ylabel('Time in milliseconds')
ax1.title('Philisophes')

ax2.plot(X2,Y2,'-g')
ax2.xlabel('Number of threads')
ax2.ylabel('Time in milliseconds')
ax2.title('Lececriv')

ax3.plot(X3,Y3,'-r')
ax1.xlabel('Number of threads')
ax1.ylabel('Time in milliseconds')
ax1.title('Philisophes')

fig.tight_layout()
plt.show()