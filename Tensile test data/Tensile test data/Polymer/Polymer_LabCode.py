# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:21:13 2023

@author: ANK

"""

import pandas as pd
import os
import statistics
import matplotlib.pyplot as plt


#----------------------------DATA-----------------------------------#

Datadic = {}

for day in range(1,3):
    if day == 1:
        limit = 13
    else:
        limit = 12
    
    for group in range(1,limit): 
    
        Path = f"Polymer_Program_Day{day}_Group{group}.xls" #BE CAREFULL WITH THE FORMAT
    
        data = pd.read_excel(Path,sheet_name="Specimen 1")
        
        
        Data_list =[]
        
        for tple in zip(data.iloc[2:,0],data.iloc[2:,1]): # Strain %
            
            Data_list.append(tple)
        
        Datadic[f"{day}.{group}"] = Data_list
        
#---------------------------DATA-------------------------------------#


# PLOTTING ONTO EACH OTHER----------------------------------------------------

# Create a new figure
plt.figure()

# Iterate over the keys and values in the dictionary
for key, value in Datadic.items():
    # Extract x and y values from each tuple
    x = [point[0] for point in value]
    y = [point[1] for point in value]
    
    # Plot the data
    plt.plot(x, y, label=key)

# Add legend and labels
plt.legend()
plt.ylabel('Stress(MPa)')
plt.xlabel('Strain(%)')

# Show the plot
plt.show()
#------------------------------------------------------------------------------

max_vals = []

for key, value in Datadic.items():
    
    max_value = max(value, key=lambda x: x[1])[1]
    max_vals.append(max_value)

print(statistics.mean(max_vals))
print(max_vals)







  