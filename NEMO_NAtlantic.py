#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:45:57 2020

@author: Tina-CTH
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import xarray as xr

#%%
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

#%%  Read file
dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')

tempA=dsTempA.THETAO
lat = np.array(tempA['LAT'].data)
depth = np.array(tempA['DEPTHT'].data)

#%%  Obtain decade average, pick latitude 20-70
A1980s = []
A1990s = []
A2000s = []
A2010s = []

#separate data into decades
for i in range(len(dsTempA['THETAO'])):
    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(1980,1990):
        for j in range(len(dsTempA['THETAO'][i])):
            A1980s.append(dsTempA['THETAO'][i][j][110:161].data)
#        A1980s.append(dsTempA['THETAO'][i].data)
#    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(1990,2000):
#        A1990s.append(dsTempA['THETAO'][i].data)
#    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(2000,2010):
#        A2000s.append(dsTempA['THETAO'][i].data)
#    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(2010,2020):
#        A2010s.append(dsTempA['THETAO'][i].data)