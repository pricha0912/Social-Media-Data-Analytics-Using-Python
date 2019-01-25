# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 07:20:48 2018

@author: Richa Patel
"""

import matplotlib.pyplot as plt
import pandas as pd

twitter_data = pd.read_csv('result5.csv')

print(twitter_data.corr())

twitter_data_subjectivity = twitter_data[twitter_data['subjectivity']>0.5]
print(twitter_data_subjectivity.corr())

#plt.scatter(twitter_data.retwc,twitter_data.polarity)
#plt.scatter(twitter_data.retwc,twitter_data.subjectivity)

plt.scatter(twitter_data.subjectivity,twitter_data.retwc)