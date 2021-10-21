#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:26:11 2020

@author: Tina-CTH
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:41:09 2020

@author: Tina-CTH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv')
years=glodap['Year'].unique()
dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
dsSaliA=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
Temp=dsTempA.THETAO
Sali=dsSaliA.SALINITY
lat = np.array(Temp['LAT'].data)
depth = np.array(Temp['DEPTHT'].data)

#uncomment this and comment out the above for Pacific
#glodap = pd.read_csv('GLODAPv2_2020_P16_Pacific.csv')
#years=glodap['Year'].unique()
#dsTemp=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Pacific_P16.nc')
#dsTempP=dsTemp.squeeze("LON211_211")
#dsSali=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Pacific_P16.nc')
#dsSaliP=dsSali.squeeze("LON211_211")
#Temp=dsTempP.THETAO
#Sali=dsSaliP.SALINITY
#lat = np.array(Temp['LAT'].data)
#depth = np.array(Temp['DEPTHT'].data)

def findM(y):  #find all months in a year in GLODAP
    g=glodap[glodap['Year']==y]
    months=g['Month'].unique()
    return months

def getMdata(y,m):  #makes new NEMO data (both temp and sali) array of chosen month
    for i in range(len(Temp)):
        Tdata=[]
        Sdata=[]
        if Temp[i].TIME_COUNTER.dt.year == y and Temp[i].TIME_COUNTER.dt.month == m:
            Tdata.append(Temp[i].data)
            Sdata.append(Sali[i].data)
            mcoord=np.array([m])
            newTarray=xr.DataArray(data=Tdata,coords=[("TIME_COUNTER",mcoord),("DEPTHT",depth),("LAT",lat)])
            newSarray=xr.DataArray(data=Sdata,coords=[("TIME_COUNTER",mcoord),("DEPTHT",depth),("LAT",lat)])
            return newTarray, newSarray

#%%
Tdata=[]      #where final data goes
Sdata=[]
latdata=[]  #NEMO latitudes
depdata=[]          #NEMO depths
ycoord=[]
mcoord=[]
#years=np.array([1988])

for y in years:
    print('year',y)
    months=findM(y)
    for m in months:
        print('month',m)
        newNEMOT, newNEMOS=getMdata(y,m)
        if len(newNEMOT) != len(newNEMOS):
            raise Exception('Check again!')        
        for i in range(len(newNEMOT)):
            for j in range(len(depth)):
                for k in range(len(lat)):
                    Tdata.append(newNEMOT[i][j][k].data)
                    Sdata.append(newNEMOS[i][j][k].data)
                    depdata.append(depth[j])
                    latdata.append(lat[k])
                    ycoord.append(y)
                    mcoord.append(m)
   
NEMO=pd.DataFrame(Tdata, columns=['Temp'])
NEMO['Sali']=Sdata
NEMO['Lat']=latdata; NEMO['Depth']=depdata
NEMO['Year']=ycoord; NEMO['Month']=mcoord