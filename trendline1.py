# https://dzone.com/articles/python-how-to-add-trend-line-to-line-chartgraph

import matplotlib.pyplot as plt

import numpy as np


import numpy as np


chris_gayle = np.array([32.44, 67.55, 61.08, 59.00, 21.77, 40.91, 22.70, 22.22, 40.88, 40.83])


rohit_sharma = np.array([28.85, 33.81, 30.92, 38.42, 30.00, 34.42, 44.45, 23.78, 23.83, 28.92])


ms_dhoni = np.array([31.88, 43.55, 29.83, 41.90, 74.20, 31.00, 40.57, 26.36, 75.83, 83.20])


virat_kohli = np.array([27.90, 46.41, 28.00, 45.28, 27.61, 45.90, 81.08, 30.80, 48.18, 33.14])



X = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])

fig, ax = plt.subplots(2, 2, figsize=(9, 7), sharex=True, sharey=True)


z = np.polyfit(X, chris_gayle, 1)


p = np.poly1d(z)


ax[1, 0].plot(X,p(X),"r--")


ax[1, 0].plot(X, chris_gayle)


ax[1, 0].set_title('Chris Gayle', fontsize=14)


# Rohit Sharma

z = np.polyfit(X, rohit_sharma, 1)


p = np.poly1d(z)


ax[0, 0].plot(X,p(X),"r--")

ax[0, 0].plot(X, rohit_sharma )

ax[0, 0].set_title('Rohit Sharma', fontsize=14)

# MS Dhoni

z = np.polyfit(X, ms_dhoni, 1)


p = np.poly1d(z)


ax[1, 1].plot(X,p(X),"r--")


ax[1, 1].plot(X, ms_dhoni)


ax[1, 1].set_title('MS Dhoni', fontsize=14)

# Virat Kohli

z = np.polyfit(X, virat_kohli, 1)

p = np.poly1d(z)

ax[0, 1].plot(X,p(X),"r--")

ax[0, 1].plot(X, virat_kohli)

ax[0, 1].set_title('Virat Kohli', fontsize=14)



fig.text(0.5, 0.04, 'Years', ha='center', fontsize=18)


fig.text(0.04, 0.5, 'Average Scores in IPL Seasons', va='center', rotation='vertical', fontsize=18)

plt.show()


