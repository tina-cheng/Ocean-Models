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

#%%

glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv')
years=glodap['Year'].unique()

dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
dsSaliA=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')

TempA=dsTempA.THETAO
SaliA=dsSaliA.SALINITY
lat = np.array(TempA['LAT'].data)
depth = np.array(TempA['DEPTHT'].data)

#%%

def findM(y):  #find all months in a year in GLODAP
    g=glodap[glodap['Year']==y]
    months=g['Month'].unique()
    return months

def findLD(y,m):  #find all latitude and depth of a month in GLODAP
    g=glodap[(glodap['Year']==y)&(glodap["Month"]==m)]
    lats=g['Latitude'].values
    deps=g['Depth'].values
    return lats, deps

def getMdata(y,m):  #makes new NEMO data (both temp and sali) array of chosen month
    for i in range(len(TempA)):
        Tdata=[]
        Sdata=[]
        if TempA[i].TIME_COUNTER.dt.year == y and TempA[i].TIME_COUNTER.dt.month == m:
            Tdata.append(TempA[i].data)
            Sdata.append(SaliA[i].data)
            mcoord=np.array([m])
            newTarray=xr.DataArray(data=Tdata,coords=[("TIME_COUNTER",mcoord),("DEPTHT",depth),("LAT",lat)])
            newSarray=xr.DataArray(data=Sdata,coords=[("TIME_COUNTER",mcoord),("DEPTHT",depth),("LAT",lat)])
            return newTarray, newSarray

def getL(l):  #get the index of NEMO latitude closest to given GLODAP latitude
    index=np.abs(lat-l).argmin()
    return index
def getD(d):  #get the index of NEMO depth closest to given GLODAP depth
    index=np.abs(depth-d).argmin()
    return index

#%%
Tdata=[]      #where final data goes
Sdata=[]
latdata=[]          #NEMO latitudes
depdata=[]          #NEMO depths
ycoord=[]
mcoord=[]
    
              
for y in years:
    print('year',y)
    months=findM(y)
    for m in months:
        print('month',m)
        lats,deps=findLD(y,m)
        newNEMOT, newNEMOS=getMdata(y,m)
        latindex=[]  #list of index of NEMO latitudes
        depindex=[]  #list of index of NEMO depths
        pairs=[]  #all locations in NEMO where there is glodap data
        for d in deps:
            index=getD(d)
            depindex.append(index)
        for l in lats:
            index=getL(l)
            latindex.append(index)   
        for i in range(len(latindex)):  #should be same as len(depindex)
            pairs.append([depindex[i],latindex[i]])
        
        grid=np.unique(pairs,axis=0)  #some locations in glodap may correspond to same point in NEMO
#        print(len(pairs))
#        print(len(grid))
        if len(newNEMOT) != len(newNEMOS):
            raise Exception('Check again!')
            
        for i in range(len(newNEMOT)):
            for j in range(len(grid)):
                indexs=grid[j]
                Tdata.append(newNEMOT[i][indexs[0]][indexs[1]].data)
                Sdata.append(newNEMOS[i][indexs[0]][indexs[1]].data)
                depdata.append(depth[indexs[0]])
                latdata.append(lat[indexs[1]])
                ycoord.append(y)
                mcoord.append(m)
        
NEMO=pd.DataFrame(Tdata, columns=['Temp'])
NEMO['Sali']=Sdata
NEMO['Lat']=latdata; NEMO['Depth']=depdata
NEMO['Year']=ycoord; NEMO['Month']=mcoord

#%%
plt.plot(latdata, depdata, 'x', label='NEMO')
plt.plot(glodap['Latitude'], glodap['Depth'], 'x', label='GLODAP')
plt.grid()
plt.legend()