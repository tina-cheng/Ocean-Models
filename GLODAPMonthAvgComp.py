#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:06:26 2020

@author: Tina-CTH
"""

import numpy as np
import matplotlib.pyplot as plt
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

#read NEMO model netcdf (.nc) file
#read .nc file using xarray (different packages are available in python)

#ds1=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
#
#ds1.keys() #to see dimensions and data variables
#salt=ds1.SALINITY
#salt.dims # check dimensions
#salt.shape # check size
#yr_mon=pd.MultiIndex.from_arrays([salt['TIME_COUNTER.year'],salt['TIME_COUNTER.month']])
#salt.coords['year_month']=('TIME_COUNTER', yr_mon)
#salt_monthavg=salt.groupby('year_month').mean()
#
##model example figure
##plt.close()
#fig,ax=plt.subplots()
#salt_monthavg[300,:,:].plot.contourf(ax=ax,cmap='viridis') #vertical profile at time=1
#ax.set_ylim(5000,0); fig.show()

#to save figure
#fig.savefig('fig.png', dpi=150, transparent = False, bbox_inches = 'tight', pad_inches = 0.1)
########################