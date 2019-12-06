# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:46:54 2019

@author: Syed Mohiuddin
"""

#   rename the cluster number with the least data point index in that cluster.

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
#from sklearn import datasets

df = pd.read_csv("normalized.csv", header = None) 

estimator = KMeans(n_clusters=7)
estimator.fit(df)

cluster_labels = estimator.labels_
test = estimator.labels_

buckets = [None] * 7

for x in range (0,527): #to get the least index in the dataset
    if buckets[cluster_labels[x]] is None:
        buckets[cluster_labels[x]] = x
    else:
        pass
    
for y in range (0,527):
    test[y] = buckets[cluster_labels[y]]
    
#np.savetxt('output.txt',test,fmt='%d')
f = open("kmeans_output.txt", "w")
for z in range (0,527):
    print(z,test[z],file = f)
    #f.write('{0} {1}'.format(z, test[z]))
    
f.close()

    
#print(buckets)

        
