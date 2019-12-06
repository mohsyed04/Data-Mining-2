# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:32:46 2019

@author: Syed Mohiuddin
"""
import csv
import numpy as np
from sklearn import preprocessing 
#import pandas as pd

with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data)

data = np.delete(data,0,1) #drop column 1
data[data == "?"] = "NAN" # replace all missing values with nan
data = data.astype('float64') # change the datatype of array 

#Replace all nan with mean
#Find indicies that you need to replace
#Place column means in the indices. Align the arrays using take
col_mean = np.nanmean(data, axis=0)
inds = np.where(np.isnan(data))
data[inds] = np.take(col_mean, inds[1]) 

data = preprocessing.normalize(data, norm='l1')

'''df = pd.DataFrame(data)
df.to_csv('normalized.csv', header=False, index=False)

import matplotlib.pyplot as plt
plt.plot(data)
plt.show()
'''
