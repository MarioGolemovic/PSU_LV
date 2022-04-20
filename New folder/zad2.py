import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# zadatak 1
mtcars=pd.read_csv('mtcars (3).csv')
print(mtcars)
mtcars.wt=mtcars.wt*100
mtcars.groupby('cyl') ['mpg']. mean().plot.bar()
mtcars.groupby('cyl') ['wt']. mean().plot.bar()
mtcars.groupby('am') ['mpg']. mean().plot.bar()
mtcars.boxplot(by='cyl', column='wt')
plt.show()