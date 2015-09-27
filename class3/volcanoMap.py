# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:03:43 2015

@author: radar
"""

import numpy as np
import matplotlib.pylab as plt
import pandas as pd 
from mpl_toolkits.basemap import Basemap


m = Basemap(projection='hammer',lon_0=180)
m.drawcoastlines(linewidth=1.25)
m.fillcontinents(color='0.8')
m.drawparallels(np.arange(-80,81,20),labels=[1,1,0,0])
m.drawmeridians(np.arange(0,360,60),labels=[0,0,0,1])

volcData = pd.DataFrame.from_csv('volcanoes.tsv', sep='\t')
x,y = m(volcData.Longitude.values,volcData.Latitude.values)
plt.scatter(x,y, marker = '^',color = 'r', s = volcData.VEI**3, zorder = 10)
plt.title('World Volcanoes')
# for the legend
l1 = plt.scatter([],[], color = 'r', marker = '^', s=2**3, edgecolors='none')
l2 = plt.scatter([],[], color = 'r', marker = '^', s=4**3, edgecolors='none')
l3 = plt.scatter([],[], color = 'r', marker = '^', s=6**3, edgecolors='none')

labels = ["2", "4", "6"]

leg = plt.legend([l1, l2, l3], labels, ncol=4, frameon=True, fontsize=12,
handlelength=2, loc = 8, borderpad = 1.8,
handletextpad=1, title='VEI', scatterpoints = 1)
plt.show()