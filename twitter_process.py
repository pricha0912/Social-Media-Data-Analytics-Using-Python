# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:28:18 2018

@author: Richa Patel
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

twitter_data = pd.read_csv('result3.csv')

plt.figure()
hist1,edges1 = np.histogram(twitter_data.friends)
plt.bar(edges1[:-1],hist1,width=edges1[1:]-edges1[:-1])

plt.scatter(twitter_data.followers,twitter_data.retwc)

