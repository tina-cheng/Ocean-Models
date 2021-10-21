#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:04:57 2020

@author: Tina-CTH
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
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
    
#%% TEMP DECADE AVERAGE  --- Atlantic

dsSali=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')

sali=dsSali.THETAO
lat = np.array(sali['LAT'].data)
depth = np.array(sali['DEPTHT'].data)


#%%  Obtain decade average
nemo_1980s = []
nemo_1990s = []
nemo_2000s = []
nemo_2010s = []

for i in range(len(dsSali['THETAO'])):
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year == 1988:
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month in range(7,9):
            nemo_1980s.append(dsSali['THETAO'][i].data)
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year in (1992, 1993):
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month in range(7,9):
            nemo_1990s.append(dsSali['THETAO'][i].data)
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year == 1998:
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month in range(4,6):
            nemo_1990s.append(dsSali['THETAO'][i].data)
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year == 2003:
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month in range(6,9):
            nemo_2000s.append(dsSali['THETAO'][i].data)
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year == 2005:
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month in range(1,3):
            nemo_2000s.append(dsSali['THETAO'][i].data)
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year == 2011:
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month == 7:
            nemo_2010s.append(dsSali['THETAO'][i].data)
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year == 2013:
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month in (8,9,10,12):
            nemo_2010s.append(dsSali['THETAO'][i].data)
    if dsSali['THETAO'][i].TIME_COUNTER.dt.year == 2014:
        if dsSali['THETAO'][i].TIME_COUNTER.dt.month == 1:
            nemo_2010s.append(dsSali['THETAO'][i].data)
#        
coord1980 = list([1980]*len(nemo_1980s))
coord1990 = list([1990]*len(nemo_1990s))
coord2000 = list([1990]*len(nemo_2000s))
coord2010 = list([1990]*len(nemo_2010s))

nemo1980sDA=xr.DataArray(data=nemo_1980s, coords=[("TIME_COUNTER",coord1980),("DEPTHT",depth),("LAT",lat)])
nemo1990sDA=xr.DataArray(data=nemo_1990s, coords=[("TIME_COUNTER",coord1990),("DEPTHT",depth),("LAT",lat)])
nemo2000sDA=xr.DataArray(data=nemo_2000s, coords=[("TIME_COUNTER",coord2000),("DEPTHT",depth),("LAT",lat)])
nemo2010sDA=xr.DataArray(data=nemo_2010s, coords=[("TIME_COUNTER",coord2010),("DEPTHT",depth),("LAT",lat)])

nemo1980sAvg = nemo1980sDA.groupby('LAT').mean('TIME_COUNTER')
nemo1990sAvg = nemo1990sDA.groupby('LAT').mean('TIME_COUNTER')
nemo2000sAvg = nemo2000sDA.groupby('LAT').mean('TIME_COUNTER')
nemo2010sAvg = nemo2010sDA.groupby('LAT').mean('TIME_COUNTER')

delta1 = np.array(nemo1990sAvg.data-nemo1980sAvg.data)
delta2 = np.array(nemo2000sAvg.data-nemo1990sAvg.data)
delta3 = np.array(nemo2010sAvg.data-nemo2000sAvg.data)

diff1=xr.DataArray(data=delta1, coords=[("DEPTHT",depth),("LAT",lat)])
diff2=xr.DataArray(data=delta2, coords=[("DEPTHT",depth),("LAT",lat)])
diff3=xr.DataArray(data=delta3, coords=[("DEPTHT",depth),("LAT",lat)])

#%%  Decade Average Plot
#gs = matplotlib.gridspec.GridSpec(2, 2, width_ratios=[0.05,0.05], height_ratios=[0.4,0.4])
#fig = plt.figure()
#fig.suptitle("Decade Average Temperature")
#
#ax1 = fig.add_subplot(gs[0])
#im = nemo1980sAvg.plot.contourf(ax=ax1,cmap='inferno', levels=30)
#ax1.set_ylim(6000,0); fig.show(); ax1.set_title('1980s')
#
#ax2 = fig.add_subplot(gs[1])
#im = nemo1980sAvg.plot.contourf(ax=ax2,cmap='inferno', levels=30)
#ax2.set_ylim(6000,0); fig.show(); ax2.set_title('1990s')
#
#ax3 = fig.add_subplot(gs[2])
#im = nemo1980sAvg.plot.contourf(ax=ax3,cmap='inferno', levels=30)
#ax3.set_ylim(6000,0); fig.show(); ax3.set_title('2000s')
#
#ax4 = fig.add_subplot(gs[3])
#im = nemo1980sAvg.plot.contourf(ax=ax4,cmap='inferno', levels=30)
#ax4.set_ylim(6000,0); fig.show(); ax4.set_title('2010s')


#%% Decade Average difference plot -- Atlantic
gs = matplotlib.gridspec.GridSpec(2, 2, width_ratios=[0.05,0.05], height_ratios=[0.4,0.4])
fig = plt.figure()
fig.suptitle("Decade Average Temperature Difference Atlantic (selected months)")

from matplotlib.colors import BoundaryNorm
#tickslabels=[-1.5,-1,-0.5,0,0.5,1,1.5]
tickslabels=np.arange(-1, 1.1,0.1)
norm=BoundaryNorm(tickslabels, len(tickslabels)-1)

ax1 = fig.add_subplot(gs[0])
im1 = diff1.plot.contourf(ax=ax1,cmap='coolwarm', norm=norm)
#plt.colorbar(im, ticks=tickslabels, spacing='proportional', extend='both')
ax1.set_ylim(6000,0); fig.show(); ax1.set_title('1990s and 1980s')

ax2 = fig.add_subplot(gs[1])
im2 = diff2.plot.contourf(ax=ax2,cmap='coolwarm', norm=norm)
ax2.set_ylim(6000,0); fig.show(); ax2.set_title('2000s and 1990s')

ax3 = fig.add_subplot(gs[2])
im3 = diff3.plot.contourf(ax=ax3,cmap='coolwarm', norm=norm)
ax3.set_ylim(6000,0); fig.show(); ax3.set_title('2010s and 2000s')