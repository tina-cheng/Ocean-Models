#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:17:31 2020

@author: Tina-CTH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import xarray as xr
from scipy.interpolate import griddata

#%% 
l_lat=50    #coords of part of north atlantic deep water
h_lat=55
l_dep=200
h_dep=600

int_x=np.arange(50,55.1,0.2, dtype=float)   #regular grid for interpolation

int_y=np.arange(100,600,10, dtype=float)

dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
dsSaliA=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')

TempA=dsTempA.THETAO
SaliA=dsSaliA.SALINITY
lat = np.array(TempA['LAT'].data)
depth = np.array(TempA['DEPTHT'].data)
years=np.unique(dsTempA.TIME_COUNTER.dt.year.data)
months=np.unique(dsTempA.TIME_COUNTER.dt.month.data)

#%%
def getD(h,l):
    index=[]
    for i in range(len(depth)):
        if l <= depth[i] <= h:
            index.append(i)
    return index
            
def getL(h,l):
    index=[]
    for i in range(len(lat)):
        if l <= lat[i] <= h:
            index.append(i)
    return index

dindex=np.array(getD(h_dep, l_dep))
lindex=np.array(getL(h_lat, l_lat))

def box(y,m):
    Tdata=[]
#    Sdata=[]
    depdata=[]
    latdata=[]
    mcoord=[]
    ycoord=[]
    for i in range(len(TempA)):
        if TempA[i].TIME_COUNTER.dt.year == y and TempA[i].TIME_COUNTER.dt.month == m:
            for j in dindex:
                for k in lindex:
                    latdata.append(lat[k])
                    depdata.append(depth[j])
                    Tdata.append(TempA[i][j][k].data)
#                    Sdata.append(SaliA[i][j][k].data)
                    mcoord.append(m)
                    ycoord.append(y)
    NEMO=pd.DataFrame(Tdata, columns=['Temp'])
#    NEMO['Sali']=Sdata
    NEMO['Lat']=latdata; NEMO['Depth']=depdata
    NEMO['Year']=ycoord; NEMO['Month']=mcoord  
    return NEMO

#%%  
Tmax=[]
maxm=[]
Tmin=[]
minm=[]
for y in years:
    print(y)
    Ts=[]
    for m in months:
        print(m)
        NEMO=box(y,m)
        t=NEMO['Temp']
        l=NEMO['Lat']
        d=NEMO['Depth']
        Nzi=griddata((l,d),t,(int_x[None,:],int_y[:,None]),method='linear', rescale=True)
        conc=np.concatenate(Nzi)
        av=[value for value in conc if value==value]
        average=np.average(av)
        Ts.append(average)
#    print(len(Ts))
    Tmax.append(Ts[np.argmax(abs(np.array(Ts)))])
    maxm.append(np.argmax(abs(np.array(Ts))))
    Tmin.append(Ts[np.argmin(abs(np.array(Ts)))])
    minm.append(np.argmin(abs(np.array(Ts))))

#%%
params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 25, 
    'axes.titlesize': 20,
    'font.size': 20, 
    'legend.fontsize': 10, 
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'figure.figsize': [15, 10],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)  
    
plt.plot(years,np.array(Tmax), 'o', color='blue',label='max')
plt.plot(years,np.array(Tmin), 'o', color='red',label='min')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Box Averaged Temperature Variation (depth 200-600, latitude 50-55), Atlantic')
plt.grid()
plt.legend()

plt.show()