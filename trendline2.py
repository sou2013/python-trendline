#use virtenv : 
#2007  conda deactivate
# 2008  source ./env2/bin/activate
# 2009  which python3


# https://stackoverflow.com/questions/41635448/how-can-i-draw-scatter-trend-line-on-matplot-python-pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv = pd.read_csv('./test.csv')
data = csv[['fee', 'time']]
x = data['fee']
y = data['time']
plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.show()
