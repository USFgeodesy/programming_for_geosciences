# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:51:12 2015

@author: radar
"""

import numpy as np
import matplotlib.pylab as plt
import pandas as pd 

# load into a dataframe which comes out as a dictionary 
rainData = pd.DataFrame.from_csv('18593LakeHanna.txt', sep='\t')
rainData.plot(x = 'Recorded Date',y = 'Aggregated Value',legend = False)
plt.title('Lake Hanna RainFaill')
plt.xlabel('Date')
plt.ylabel('Inches') 
plt.savefig('rain.png',dpi=600)
plt.show()
