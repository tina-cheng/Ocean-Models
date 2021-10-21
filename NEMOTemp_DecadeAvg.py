#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 05:28:07 2020

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
    
#%% TEMP DECADE AVERAGE
dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
dsTemp=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Pacific_P16.nc')
dsTempP=dsTemp.squeeze("LON211_211")


tempA=dsTempA.THETAO
lat = np.array(tempA['LAT'].data)
depth = np.array(tempA['DEPTHT'].data)

#%%  Obtain decade average
A1980s = []
A1990s = []
A2000s = []
A2010s = []
P1980s = []
P1990s = []
P2000s = []
P2010s = []

#separate data into decades
for i in range(len(dsTempA['THETAO'])):
    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(1980,1990):
        A1980s.append(dsTempA['THETAO'][i].data)
    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(1990,2000):
        A1990s.append(dsTempA['THETAO'][i].data)
    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(2000,2010):
        A2000s.append(dsTempA['THETAO'][i].data)
    if dsTempA['THETAO'][i].TIME_COUNTER.dt.year in range(2010,2020):
        A2010s.append(dsTempA['THETAO'][i].data)
        
for i in range(len(dsTempP['THETAO'])):
    if dsTempP['THETAO'][i].TIME_COUNTER.dt.year in range(1980,1990):
        P1980s.append(dsTempP['THETAO'][i].data)
    if dsTempP['THETAO'][i].TIME_COUNTER.dt.year in range(1990,2000):
        P1990s.append(dsTempP['THETAO'][i].data)
    if dsTempP['THETAO'][i].TIME_COUNTER.dt.year in range(2000,2010):
        P2000s.append(dsTempP['THETAO'][i].data)
    if dsTempP['THETAO'][i].TIME_COUNTER.dt.year in range(2010,2020):
        P2010s.append(dsTempP['THETAO'][i].data)
     
#create new coordinate based on decades
coord1980 = list([1980]*len(P1980s))
coord1990 = list([1990]*len(P1990s))
coord2000 = list([1990]*len(P2000s))
coord2010 = list([1990]*len(P2010s))
lon = np.array([210])

#make new data arrays with new coordinates
A1980sDA=xr.DataArray(data=A1980s, coords=[("TIME_COUNTER",coord1980),("DEPTHT",depth),("LAT",lat)])
A1990sDA=xr.DataArray(data=A1990s, coords=[("TIME_COUNTER",coord1990),("DEPTHT",depth),("LAT",lat)])
A2000sDA=xr.DataArray(data=A2000s, coords=[("TIME_COUNTER",coord2000),("DEPTHT",depth),("LAT",lat)])
A2010sDA=xr.DataArray(data=A2010s, coords=[("TIME_COUNTER",coord2010),("DEPTHT",depth),("LAT",lat)])
P1980sDA=xr.DataArray(data=P1980s, coords=[("TIME_COUNTER",coord1980),("DEPTHT",depth),("LAT",lat)])
P1990sDA=xr.DataArray(data=P1990s, coords=[("TIME_COUNTER",coord1990),("DEPTHT",depth),("LAT",lat)])
P2000sDA=xr.DataArray(data=P2000s, coords=[("TIME_COUNTER",coord2000),("DEPTHT",depth),("LAT",lat)])
P2010sDA=xr.DataArray(data=P2010s, coords=[("TIME_COUNTER",coord2010),("DEPTHT",depth),("LAT",lat)])

#get average of each array, group by latitude, ignoring year
A1980sAvg = A1980sDA.groupby('LAT').mean('TIME_COUNTER')
A1990sAvg = A1990sDA.groupby('LAT').mean('TIME_COUNTER')
A2000sAvg = A2000sDA.groupby('LAT').mean('TIME_COUNTER')
A2010sAvg = A2010sDA.groupby('LAT').mean('TIME_COUNTER')
P1980sAvg = P1980sDA.groupby('LAT').mean('TIME_COUNTER')
P1990sAvg = P1990sDA.groupby('LAT').mean('TIME_COUNTER')
P2000sAvg = P2000sDA.groupby('LAT').mean('TIME_COUNTER')
P2010sAvg = P2010sDA.groupby('LAT').mean('TIME_COUNTER')

#get difference between decade averages
Adelta1 = np.array(A1990sAvg.data-A1980sAvg.data)
Adelta2 = np.array(A2000sAvg.data-A1990sAvg.data)
Adelta3 = np.array(A2010sAvg.data-A2000sAvg.data)
Pdelta1 = np.array(P1990sAvg.data-P1980sAvg.data)
Pdelta2 = np.array(P2000sAvg.data-P1990sAvg.data)
Pdelta3 = np.array(P2010sAvg.data-P2000sAvg.data)

#make new data arrays with differences
Adiff1=xr.DataArray(data=Adelta1, coords=[("DEPTHT",depth),("LAT",lat)])
Adiff2=xr.DataArray(data=Adelta2, coords=[("DEPTHT",depth),("LAT",lat)])
Adiff3=xr.DataArray(data=Adelta3, coords=[("DEPTHT",depth),("LAT",lat)])
Pdiff1=xr.DataArray(data=Pdelta1, coords=[("DEPTHT",depth),("LAT",lat)])
Pdiff2=xr.DataArray(data=Pdelta2, coords=[("DEPTHT",depth),("LAT",lat)])
Pdiff3=xr.DataArray(data=Pdelta3, coords=[("DEPTHT",depth),("LAT",lat)])

#%%  Decade Average Plot
#gs = matplotlib.gridspec.GridSpec(2, 2, width_ratios=[0.05,0.05], height_ratios=[0.4,0.4])
#fig = plt.figure()
#fig.suptitle("Decade Average Temperature")
#
#ax1 = fig.add_subplot(gs[0])
#im = P1980sAvg.plot.contourf(ax=ax1,cmap='inferno', levels=30)
#ax1.set_ylim(6000,0); fig.show(); ax1.set_title('1980s')
#
#ax2 = fig.add_subplot(gs[1])
#im = P1990sAvg.plot.contourf(ax=ax2,cmap='inferno', levels=30)
#ax2.set_ylim(6000,0); fig.show(); ax2.set_title('1990s')
#
#ax3 = fig.add_subplot(gs[2])
#im = P2000sAvg.plot.contourf(ax=ax3,cmap='inferno', levels=30)
#ax3.set_ylim(6000,0); fig.show(); ax3.set_title('2000s')
#
#ax4 = fig.add_subplot(gs[3])
#im = P2010sAvg.plot.contourf(ax=ax4,cmap='inferno', levels=30)
#ax4.set_ylim(6000,0); fig.show(); ax4.set_title('2010s')

#%% Decade Average difference plot -- Atlantic
gs = matplotlib.gridspec.GridSpec(2, 2, width_ratios=[0.05,0.05], height_ratios=[0.4,0.4])
fig = plt.figure(1)
fig.suptitle("Decade Averaged Temperature Difference Atlantic")

from matplotlib.colors import BoundaryNorm
tickslabels=np.arange(-1,1.1,0.1)
norm=BoundaryNorm(tickslabels, len(tickslabels)-1)

ax1 = fig.add_subplot(gs[0])
im1 = Adiff1.plot.contourf(ax=ax1,cmap='coolwarm', norm=norm)
ax1.set_ylim(6000,0); fig.show(); ax1.set_title('1990s and 1980s')
plt.grid()
ax2 = fig.add_subplot(gs[1])
im2 = Adiff2.plot.contourf(ax=ax2,cmap='coolwarm', norm=norm)
ax2.set_ylim(6000,0); fig.show(); ax2.set_title('2000s and 1990s')
plt.grid()
ax3 = fig.add_subplot(gs[2])
im3 = Adiff3.plot.contourf(ax=ax3,cmap='coolwarm', norm=norm)
ax3.set_ylim(6000,0); fig.show(); ax3.set_title('2010s and 2000s')
plt.grid()

#%%  Decade Average difference plot -- Pacific
fig = plt.figure(2)
fig.suptitle("Decade Averaged Temperature Difference Pacific")
tickslabels=np.arange(-0.5,0.505,0.05)
norm=BoundaryNorm(tickslabels, len(tickslabels)-1)

ax1 = fig.add_subplot(gs[0])
im1 = Pdiff1.plot.contourf(ax=ax1,cmap='coolwarm', norm=norm)
ax1.set_ylim(6000,0); fig.show(); ax1.set_title('1990s and 1980s')

ax2 = fig.add_subplot(gs[1])
im2 = Pdiff2.plot.contourf(ax=ax2,cmap='coolwarm', norm=norm)
ax2.set_ylim(6000,0); fig.show(); ax2.set_title('2000s and 1990s')

ax3 = fig.add_subplot(gs[2])
im3 = Pdiff3.plot.contourf(ax=ax3,cmap='coolwarm', norm=norm)
ax3.set_ylim(6000,0); fig.show(); ax3.set_title('2010s and 2000s')
