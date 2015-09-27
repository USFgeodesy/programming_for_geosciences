# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:51:12 2015

@author: radar
"""

import numpy as np
import matplotlib.pylab as plt
import pandas as pd 

rainData = pd.DataFrame.from_csv('18593LakeHanna.txt', sep='\t',header = 1)