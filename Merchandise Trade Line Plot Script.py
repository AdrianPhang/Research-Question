# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:43:30 2019

@author: phang
"""
# Importing Library (CSV, Panda and Matplotlib)
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Importing MT CSV file over to Python
df = pd.read_csv( 'MT.csv' )
mt = []

# Arranging the data lines and appending it downwards
with open ( "MT.csv", "r" ) as csv_file:
    csv_reader = csv.reader ( csv_file, delimiter=',' )
    for lines in csv_reader:
        mt.append(lines)
    
# Converting figures into floating numbers    
mt[1] = [ float(i) for i in mt[1] ]

# Printing of the data sets
print ( mt[0] )

# Setting the limit for Y axis
plt.ylim ( 60000 , 100000 )

# Add title and axis names
plt.title ( 'Merchandise Trade per Year' )
plt.xlabel ( 'Year' )
plt.ylabel ( 'SGD$' )

# Plot the graph with the 2 data sets
plt.plot(mt[0],mt[1])

# Create a Dictionary of series
d = {'Year':pd.Series(mt[0]),
   'SGD$':pd.Series(mt[1])}
 
# Create a DataFrame for Summary Statistics
df = pd.DataFrame(d)
print ( df )
print ( df.describe() )