#!/usr/bin/env python
# coding: utf-8

# In[42]:


"Author ANK"


# In[55]: MEAN CALCULATOR FOR RESULTS SHEET


import pandas as pd
import os
import statistics
import matplotlib.pyplot as plt
os.getcwd()
os.chdir('C:\\Users\\Misafir\\Desktop\\ME232 LAB\\Tensile test data\\Tensile test data\\Metal')


#--------------------------- DATA-----------------------------------------------

Datadic = {}

for day in range(1,3):
    if day == 1:
        limit = 13
    else:
        limit = 12
    
    for group in range(1,limit): 
    
        Path = f"Metal_St_Program_Day{day}_Group{group}.xls" #BE CAREFULL WITH THE FORMAT
    
        data = pd.read_excel(Path,sheet_name="Specimen 1")
        
        
        Data_list =[]
        
        for tple in zip(data.iloc[2:,0],data.iloc[2:,1]): # Strain %
            
            Data_list.append(tple)
        
        Datadic[f"{day}.{group}"] = Data_list
        
#----------------------------DATA-------------------------------------------


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

#----------------------------------------------------------------------------



# CALCULATE MEAN FOR E---------------------------------------------------------
uppervaldic = {}

for key, value in Datadic.items():
    for tple in value:
        if tple[1] > 150 and tple[0]>0:
            uppervaldic[key] = tple
            break
lowervaldic = {}

for key, value in Datadic.items():
    for tple in value:
        if tple[1] > 50:
            lowervaldic[key] = tple
            break      

E_val = []

for key, value in uppervaldic.items():
     lowpoint = lowervaldic[key]
     
     E_cal = ((value[1]-lowpoint[1])*10**(6)/(value[0]*0.01-lowpoint[0]*0.01))*0.000000001
     E_val.append(float(f"{E_cal:.2f}"))
     
print(E_val)
print(f"{statistics.mean(E_val):.2f}")



# CALCULATE MEAN FOR ULTIMATE STRESS---------------------------------------------
max_vals = []

for key, value in Datadic.items():
    
    max_value = max(value, key=lambda x: x[1])[1]
    max_vals.append(max_value)

print(statistics.mean(max_vals))
print(max_vals)

#--------------------------------------------------------------------------------
        