import pandas as pd
import numpy as np

np.random.seed(1)
#Declare date 0
date0 = np.datetime64('2020-01-01')
#Declare date 1
date1 = np.datetime64('2020-06-30')

#Generate a list of dates
datelist = pd.date_range(date0, date1, freq = 'M') 
#M = Month, MS = Start of the month, WOM-3Fri = Week of month- 3rd friday, Google Date Range

print(datelist)

#Generate array of 6 rows and 5 columns > Creating Data Frame
data = np.random.randint(1,100,size=[6,5])

#create data frame
x = pd.DataFrame(data, index = datelist, columns = list('ABCDE'))

print(x)
