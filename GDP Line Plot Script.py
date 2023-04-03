# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:12:19 2019

@author: phang
"""
# Importing Libraries (CSV,Pandas and Matplotlib)
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Import GDP CSV File
df = pd.read_csv( 'GDP.csv' )
my_list = []

# Arranging the data lines and appending it downwards
with open( "GDP.csv", "r" ) as csv_file:
    csv_reader = csv.reader ( csv_file, delimiter=',' )
    for lines in csv_reader:
        my_list.append ( lines )
    
# Converting figures into floating numbers    
my_list[1] = [ float ( i ) for i in my_list[1] ]

# Printing of the data set
print ( my_list[0] )

# Setting the limit for Y axis
plt.ylim ( 90000,130000 )

# Add title and axis names
plt.title ( 'Gross Domestic Product per Year' )
plt.xlabel ( 'Year' )
plt.ylabel ( 'SGD$' )

# Plot the graph with the 2 data sets
plt.plot ( my_list[0] , my_list[1] )


# Create a Dictionary of series
d = { 'Year':pd.Series(my_list[0]),
   ' SGD$ ':pd.Series(my_list[1]) }
 
# Create a DataFrame for Summary Statistics
df = pd.DataFrame( d )
print ( df )
print ( df.describe() ) 
