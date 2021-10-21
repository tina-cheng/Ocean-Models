#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 05:11:23 2020

@author: Tina-CTH
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import xarray as xr

#read csv data
glodap  = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv')
#either assign each data to a single variable (optional)
cruise  = glodap['Cruise']; depth = glodap['Depth']; lat = glodap['Latitude']; lon = glodap['Longitude']
month   = glodap['Month']; year = glodap['Year']
salt    = glodap['Salinity']; temp = glodap['Temperature']; density = glodap['Sigma0']

#or create a dataframe
data=glodap[['Year','Month','Latitude','Depth','Salinity']]
data=data['Salinity'].groupby([data.Year,data.Month,data.Latitude,
         data.Depth]).mean().rename('Mean Salinity').reset_index()

glodapyr = []
for x in glodap['Year']:
    if x not in glodapyr:
        glodapyr.append(x)
print(glodapyr)

#glodap example figure
#fig,ax=plt.subplots()
#data.plot.scatter(ax=ax,x='Latitude',y='Depth',c='Mean Salinity',colormap='viridis') #vertical profile full data
#ax.set_ylim(5000,0); fig.show()
#%%
#read NEMO model netcdf (.nc) file
#read .nc file using xarray (different packages are available in python)
ds1=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')

ds1.keys() #to see dimensions and data variables
salt=ds1.SALINITY
salt.dims # check dimensions
salt.shape # check size

sali1988=ds1['SALINITY'].sel(TIME_COUNTER='1988')
sali1998=ds1['SALINITY'].sel(TIME_COUNTER='1998')
delta=np.array(sali1988.data-sali1998.data)

months = np.array(sali1988['TIME_COUNTER.month'].data)
lat = np.array(salt['LAT'].data)
depth = np.array(salt['DEPTHT'].data)

diff=xr.DataArray(data=delta, coords=[("TIME_COUNTER",months),("DEPTHT",depth),("LAT",lat)])


#yr_mon=pd.MultiIndex.from_arrays([salt['TIME_COUNTER.year'],salt['TIME_COUNTER.month']])
#salt.coords['year_month']=('TIME_COUNTER', yr_mon)
#salt_monthavg=salt.groupby('year_month').mean()

params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 10, # fontsize for x and y labels (was 10)
    'axes.titlesize': 8,
    'font.size': 10, # was 10
    'legend.fontsize': 10, # was 10
    'xtick.labelsize': 5,
    'ytick.labelsize': 5,
    'figure.figsize': [15, 25],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)
#%%
#model example figure
fig = plt.figure()
fig.suptitle("1988 & 1998 Salinity")
gs = matplotlib.gridspec.GridSpec(5, 2, width_ratios=[0.05,0.05], height_ratios=[0.4,0.4,0.4,0.4,0.4])
gs.update(wspace=0.4, hspace=0.20)

for i in range(10):
    ax = fig.add_subplot(gs[i])
    im = diff[i,:,:].plot.contourf(ax=ax,cmap='coolwarm', levels=15, vmin=-0.5, vmax=0.5)
    ax.set_ylim(6000,0); fig.show()


#to save figure
#fig.savefig('fig.png', dpi=150, transparent = False, bbox_inches = 'tight', pad_inches = 0.1)
########################
    
