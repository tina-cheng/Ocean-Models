#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:33:02 2020

@author: Tina-CTH
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import xarray as xr


ds1=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')

ds1.keys() #to see dimensions and data variables
salt=ds1.THETAO
salt.dims # check dimensions
salt.shape # check size

allyears = np.array(salt['TIME_COUNTER.year'].data)
years = []
for i in range(len(allyears)):
    if allyears[i] not in years:
        years.append(allyears[i])

allmonths = np.array(salt['TIME_COUNTER.month'].data)
months = []
for i in range(len(allmonths)):
    if allmonths[i] not in months:
        months.append(allmonths[i])
        
lat = np.array(salt['LAT'].data)
depth = np.array(salt['DEPTHT'].data)

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

fig = plt.figure()
fig.suptitle("1993 Surface Temperature Variation")
gs = matplotlib.gridspec.GridSpec(6, 2, width_ratios=[0.05,0.05], height_ratios=[0.4,0.4,0.4,0.4,0.4,0.4])
gs.update(wspace=0.4, hspace=0.20)


temp1981 = ds1['THETAO'].sel(TIME_COUNTER='1993')
#delta = temp1981[5].data - temp1981[0].data
for i in range(11):
    ax = fig.add_subplot(gs[i])
    delta = temp1981[i+1].data-temp1981[i].data
    diff=xr.DataArray(data=delta, coords=[("DEPTHT",depth),("LAT",lat)])
    surf_diff = diff.where(diff.DEPTHT < 200, drop=True)
    surf_diff.plot.contourf(cmap='coolwarm', levels=20,vmax=3.5,vmin=-3.5)
    plt.title(i+1)
    ax.set_ylim(200,0); fig.show()
#    
#delta = (sali2.data-sali1.data)[0]
#
#diff=xr.DataArray(data=delta, coords=[("DEPTHT",depth),("LAT",lat)])
#surf_diff = diff.where(diff.DEPTHT < 200, drop=True)
#surf_diff.plot.contourf(cmap='coolwarm', levels=20)
#plt.ylim(200,0)