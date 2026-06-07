# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:24:59 2023

@author: AHMET NURİ KİRİŞCİ
"""

import pandas as pd
import os
import statistics
import matplotlib.pyplot as plt
import math

#list format [L,a,w,t]

Specimen_1 = [0.26,0.007,0.02,0.004]
Specimen_2 = [0.26,0.005,0.02,0.004]
Specimen_3 = [0.224,0.005,0.02,0.004]
Specimen_4 = [0.224,0.007,0.02,0.004]

Specimen_pro = [Specimen_1, Specimen_2, Specimen_3, Specimen_4]

#DATA DICTIONARY IS CREATED FOR FURTHER USE
#--------------------------------------------------------------------------------------------

Path = f"Fracture data.xlsx" #BE CAREFULL WITH THE FORMAT

data = pd.read_excel(Path,sheet_name="Sheet1")

DataDic = {}

for col in range (1,5):
    datas = []
    for value in data.iloc[0:,col]:
        if str(value) != "nan": 
            datas.append(float(value))
    
    DataDic[f"Specimen{col}"] = datas
#-----------------------------------------------------------------------------------------

#CALCULATIONS-------------------------------------------------------------------------------

Frac_dic = {}

for i in range(0,4):
    
    fracture = []
        
    for data_index in range(0,23):
    
        alfa = Specimen_pro[i][1]/Specimen_pro[i][2]
        
        if alfa <= 0.4:
            #print(alfa,"Assumption Holds")
            Formf = 1.12
        
        Moment = (9.81*DataDic[f"Specimen{i+1}"][data_index]) * 0.5 * (Specimen_pro[i][0]/2)
        
        #print(Moment)
        
        gross = (6*Moment)/((20*10**(-3))**(2)*4*10**(-3))
        #print(gross*10**(-6))
        
        Fracture = Formf * (gross)*math.sqrt(math.pi*(Specimen_pro[i][1]))
        
        fracture.append(Fracture*10**(-6))
    
    Frac_dic[f"Specimen{i+1}"] = fracture

# FRACTURE TOUGHNESS VALUES FOR CHOOSEN GROUP DATA-------------------------------------------------------

print("DAY4 GROUP1 SPECIMEN FRACTURE TOUGHNESSE")
print(Frac_dic["Specimen1"][12])
print(Frac_dic["Specimen2"][12])
print(Frac_dic["Specimen3"][12])
print(Frac_dic["Specimen4"][12])


#------------------------------------------------------------------------------------------------------------------ 
    
    
    
 
#PRINTS THE VALUES WHICH IS DESIRED--------------------------------------------------------------------------------
print("MEAN VALUES FOR EACH SPECIMEN AS IN THE ORDER 1,2,3,4")
print(str(statistics.mean(Frac_dic["Specimen1"]))+"\n"+str(statistics.mean(Frac_dic["Specimen2"]))+"\n"+str(statistics.mean(Frac_dic["Specimen3"]))+"\n"+str(statistics.mean(Frac_dic["Specimen4"])))
print()
print("STANDARD DEVIATION VALUES FOR EACH SPECIMEN AS IN THE ORDER 1,2,3,4")
print(str(statistics.stdev(Frac_dic["Specimen1"]))+"\n"+str(statistics.stdev(Frac_dic["Specimen2"]))+"\n"+str(statistics.stdev(Frac_dic["Specimen3"]))+"\n"+str(statistics.stdev(Frac_dic["Specimen4"])))

#----------------------------------------------------------------------------------------------------------------------------------------


"""

"Specimen_pro" list contains the properties of the each specimen list within list format

"Frac_dic" dictionary contains calculated fracture toughness value for each specimen, keys are the specimen names

"Data_dic" dictionary contains excel data for each specimen, keys are the specimen names

Note : for code to work properly code file and the excel file must be in the same folder

"""


#PLOTTING------------------------------------------------------------------

fig, ax = plt.subplots()

# Plot the data from the dictionary
for key, values in Frac_dic.items():
    ax.plot(values, label=key)

# Add legend
ax.legend()

# Show the plot
plt.show()


#--------------------------------------------------------------------------









