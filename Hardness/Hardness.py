# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:43:28 2023

@author: Misafir
"""
# IMPORTING REQUIRED LIBRARIES------------------------------

import pandas as pd
import os
import statistics
import matplotlib.pyplot as plt
import math
#------------------------------------------------------------

#CONSTANT VARIABLES-----------------------------------------

S1 = "Steel"
S2 = "Copper"
S3 = "Aluminum"
#-----------------------------------------------------------

#DATA ACQUIRE------------------------------------------------

data = pd.read_excel("vickers.xlsx",sheet_name="Sheet1")


DataDic = {}

for col in range (4,11,3):
    datas = []
    for value in data.iloc[4:,col]:
        if str(value) != "nan" and str(value) != "HV": 
            datas.append(float(value))
    if col == 4:
        
        DataDic[S1] = datas
    elif col == 7:
        DataDic[S2] = datas
    
    else:
        DataDic[S3] = datas

#print(DataDic)
#---------------------------------------------------------------

#MEAN AND STDEV CALCULATIN RESULTS------------------------------------
print("-----------METAL VICKERS/BRINELL-------------------")
for key in DataDic:
    
    print(key+"MEAN:"+" "+str(statistics.mean(DataDic[key])))
    
    print(key+"STDEV:"+" "+str(statistics.stdev(DataDic[key]))+"\n")
    
#-----------------------------------------------------------------------

#FORMULA CHECK FOR SECOND QUESTION--------------------------------------
"""
d1 = float(input("Enter d1: "))
d2 = float(input("Enter d2: "))

d12 = ((d1*10**(-3))+(d2*10**(-3)))/2

P = 1 # kgf

HV = (1.8544*P)/(d12)**2

print(HV)
"""
#------------------------------------------------------------------------    
print("----POLYMER SHORE------------")
#POLYMER DATA ACQUIRE----------------------------------------------------
P1 = "Silicone"
P2 = "PDMS"
P3 = "MRE"

data_polymer = pd.read_excel("shore.xlsx",sheet_name="Sheet1")

DataDic_polymer = {}
for col in range(2,5):
    
    datas_polymer = []
    
    for value in data_polymer.iloc[4:,col]:
        
        if str(value) != "nan": 
            datas_polymer.append(float(value))      
    if col == 2:
        DataDic_polymer[P1] = datas_polymer
        print(f"Mean {P1}: "+str(statistics.mean(datas_polymer)))
        print(f"STDev {P1}: "+str(statistics.stdev(datas_polymer)))
        print("-------------------------------------------")
    elif col == 3:
        DataDic_polymer[P2] = datas_polymer
        print(f"Mean {P2}: "+str(statistics.mean(datas_polymer)))
        print(f"STDev {P2}: "+str(statistics.stdev(datas_polymer)))
        print("-------------------------------------------")
    else:
        DataDic_polymer[P3] = datas_polymer
        print(f"Mean {P3}: "+str(statistics.mean(datas_polymer)))
        print(f"STDev {P3}: "+str(statistics.stdev(datas_polymer)))
        print("-------------------------------------------")

#print(DataDic_polymer)
#------------------------------------------------------------------------

# POLYMER SHORE DUROMETER CALCULATION------------------------------------

d= 0.79*10**(-3)
c1 = 0.549 #N
c2 = 0.07516 #N
c3 = 0.025*10**(-3)

alfa = 4*d*c3

Datadic_polyE = {}

for keys in DataDic_polymer:
    evalues = []
    
    for values in DataDic_polymer[keys]:
        
        E = ((3/alfa)*((c1+c2*values)/(100-values)))*10**(-3)
        
        evalues.append((E,values))
    
    Datadic_polyE[keys] = evalues


print(Datadic_polyE)


fig, ax = plt.subplots()

# Plot the data from the dictionary
for key, values in Datadic_polyE.items():
    x_values = [t[1] for t in values]  # Extract x-values from tuples
    y_values = [t[0] for t in values]  # Extract y-values from tuples
    ax.scatter(x_values, y_values, label=key)

# Add legend
ax.legend()
plt.ylabel('E(KPa)')
plt.xlabel('S')

# Show the plot
plt.show()

#------------------------------------------------------------------------
#-----------------------E(0) CALCULATIN--------------------------------Ğ
print()
print("-----------E(0) CALCULATION----------------")




d= 0.79*10**(-3)
c1 = 0.549 #N
c2 = 0.07516 #N
c3 = 0.025*10**(-3)

alfa = 4*d*c3


E = ((3/alfa)*((c1+c2*0)/(100-0)))*10**(-3)

print(E)







    