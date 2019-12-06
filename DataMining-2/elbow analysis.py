# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:54:04 2019

@author: Syed Mohiuddin
"""
###########  https://predictivehacks.com/k-means-elbow-method-code-for-python/ ##########
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("normalized.csv", header = None)

distortions = []
K = range(1,38)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(df)
    distortions.append(kmeanModel.inertia_)
    
plt.figure(figsize=(16,8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()