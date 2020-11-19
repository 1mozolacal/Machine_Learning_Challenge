# example from https://python-graph-gallery.com/122-multiple-lines-chart/
# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Data
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21) })
print(df)
# multiple line plot
plt.plot( 'x', 'y1','', data=df, marker='o',  linewidth=4)
plt.plot( 'x', 'y2','', data=df, marker='1',  linewidth=2)
plt.plot( 'x', 'y3','', data=df, marker='',  linewidth=2, linestyle='dashed', label="toto")
plt.legend()
plt.show()

'''
The third parameter is the formating string, it is being passed as black to suppress warning message
'''

# marker reference
# https://matplotlib.org/api/markers_api.html