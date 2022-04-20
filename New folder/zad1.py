import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#1
mtcars=pd.read_csv('mtcars (3).csv')

print(mtcars.sort_values(by=['mpg']).head(5))
#2
print(mtcars[mtcars.cyl==8].sort_values(by=['mpg']).tail(3))
#3
print(mtcars[mtcars.cyl==6].mpg.mean())
#4
print(mtcars[(mtcars.cyl==4) & (mtcars.wt>2.0) & (mtcars.wt<2.2)].mpg.mean())
#5
print(mtcars[(mtcars.am==True) & (mtcars.hp>100)].count().car)
#6
mtcars_new=mtcars[(mtcars.am==0)&(mtcars.hp>100)]
print("automatski mjenjaci", len(mtcars_new))

#7
mtcars['kg']=mtcars.wt*1000*0.453
print(mtcars)







