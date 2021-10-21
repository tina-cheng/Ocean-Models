#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 02:01:54 2020

@author: Tina-CTH
"""

import numpy as np
import matplotlib.tri as tri
import matplotlib.gridspec
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr


#glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv')
#j_1980s = glodap[(glodap['Year']==1988)&(glodap["Month"]==7)]
#j_1990s = glodap[(glodap['Year'].between(1990,2000, inclusive= False))&(glodap["Month"]==7)]
#j_2000s = glodap[(glodap['Year'].between(2000,2010, inclusive= False))&(glodap["Month"]==7)]
#j_2010s = glodap[(glodap['Year'].between(2010,2020, inclusive= False))&(glodap["Month"]==7)]
#
#
#
#params = {
#    'image.cmap': 'Blues',
#    'axes.labelsize': 20, # fontsize for x and y labels (was 10)
#    'axes.titlesize': 20,
#    'font.size': 20, # was 10
#    'legend.fontsize': 20, # was 10
#    'xtick.labelsize': 20,
#    'ytick.labelsize': 20,
#    'figure.figsize': [15, 15],
#    'font.family': 'serif',
#}
#
##updating parameters for plotting
#matplotlib.rcParams.update(params)
#
#
#
#x_1990s = j_1990s['Latitude']
#y_1990s = (-j_1990s['Depth'])
#z_1990s = j_1990s['Temperature']
#
#fig, (ax1, ax2) = plt.subplots(nrows=2)
#
## -----------------------
## Interpolation on a grid
## -----------------------
## A contour plot of irregularly spaced data coordinates
## via interpolation on a grid.
#
## Create grid values first.
#xi = np.linspace(-45, 15, 60)
#yi = np.linspace(-6000, 0, 600)
#
## Perform linear interpolation of the data (x,y)
## on a grid defined by (xi,yi)
#triang = tri.Triangulation(x_1990s, y_1990s)
#interpolator = tri.LinearTriInterpolator(triang, z_1990s)
#Xi, Yi = np.meshgrid(xi, yi)
#zi = interpolator(Xi, Yi)
#
## Note that scipy.interpolate provides means to interpolate data on a grid
## as well. The following would be an alternative to the four lines above:
##from scipy.interpolate import griddata
##zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='linear')
#
#
#ax1.contour(xi, yi, zi, levels=60, linewidths=0.5, colors='k')
#cntr1 = ax1.contourf(xi, yi, zi, levels=60, cmap="nipy_spectral")
#
#fig.colorbar(cntr1, ax=ax1)
#ax1.plot(x_1990s, y_1990s, 'ko', ms=3)
#ax1.set(xlim=(-45, 15), ylim=(-6000, 0))
#ax1.set_title('grid and contour ( %d grid points)' %
#              ( 60 * 600))
#
## ----------
## Tricontour
## ----------
## Directly supply the unordered, irregularly spaced coordinates
## to tricontour.
#
#ax2.tricontour(x_1990s, y_1990s, z_1990s, levels=60, linewidths=0.5, colors='k')
#cntr2 = ax2.tricontourf(x_1990s, y_1990s, z_1990s, levels=60, cmap="nipy_spectral")
#
#fig.colorbar(cntr2, ax=ax2)
#ax2.plot(x_1990s, y_1990s, 'ko', ms=3)
#ax2.set(xlim=(-45, 15), ylim=(-6000, 0))
#ax2.set_title('tricontour')
#
#plt.subplots_adjust(hspace=0.5)
#plt.show()



params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 20, # fontsize for x and y labels (was 10)
    'axes.titlesize': 20,
    'font.size': 20, # was 10
    'legend.fontsize': 20, # was 10
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'figure.figsize': [15, 15],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)

#%%

#x_2010s = j_2010s['Latitude']
#y_2010s = (-j_2010s['Depth'])
#z_2010s = j_2010s['Temperature']
#
#fig, ax = plt.subplots(6, sharex=True, gridspec_kw={'hspace': 0.2})
#fig.suptitle('July 2010s Interpolated')
#
#ax[0].tricontour(x_2010s, y_2010s, z_2010s, levels=60, linewidths=0.5, colors='k')
#cntr1 = ax[0].tricontourf(x_2010s, y_2010s, z_2010s, levels=60, cmap="nipy_spectral")
#
#ax[0].plot(x_2010s, y_2010s, 'ko', ms=3)
#ax[0].set(xlim=(20, 50), ylim=(-100, 0))
#
#
#ax[1].tricontour(x_2010s, y_2010s, z_2010s, levels=60, linewidths=0.5, colors='k')
#cntr2 = ax[1].tricontourf(x_2010s, y_2010s, z_2010s, levels=60, cmap="nipy_spectral")
#
#ax[1].plot(x_2010s, y_2010s, 'ko', ms=3)
#ax[1].set(xlim=(20, 50), ylim=(-500, -100))
#
#ax[2].tricontour(x_2010s, y_2010s, z_2010s, levels=60, linewidths=0.5, colors='k')
#cntr3 = ax[2].tricontourf(x_2010s, y_2010s, z_2010s, levels=60, cmap="nipy_spectral")
#
#ax[2].plot(x_2010s, y_2010s, 'ko', ms=3)
#ax[2].set(xlim=(20, 50), ylim=(-1000, -500))
#
#ax[3].tricontour(x_2010s, y_2010s, z_2010s, levels=60, linewidths=0.5, colors='k')
#cntr4 = ax[3].tricontourf(x_2010s, y_2010s, z_2010s, levels=60, cmap="nipy_spectral")
#
#ax[3].plot(x_2010s, y_2010s, 'ko', ms=3)
#ax[3].set(xlim=(20, 50), ylim=(-2500, -1000))
#
#ax[4].tricontour(x_2010s, y_2010s, z_2010s, levels=60, linewidths=0.5, colors='k')
#cntr5 = ax[4].tricontourf(x_2010s, y_2010s, z_2010s, levels=60, cmap="nipy_spectral")
#
#ax[4].plot(x_2010s, y_2010s, 'ko', ms=3)
#ax[4].set(xlim=(20, 50), ylim=(-4000, -2500))
#
#ax[5].tricontour(x_2010s, y_2010s, z_2010s, levels=60, linewidths=0.5, colors='k')
#cntr6 = ax[5].tricontourf(x_2010s, y_2010s, z_2010s, levels=60, cmap="nipy_spectral")
#
#ax[5].plot(x_2010s, y_2010s, 'ko', ms=3)
#ax[5].set(xlim=(20, 50), ylim=(-6000, -4000))
#
#fig.colorbar(cntr6, ax=ax)
#
#for axs in ax:
#    axs.label_outer()
#   
#plt.xlabel('Latitude')
#
#
#plt.show()

#%%   using griddata
from scipy.interpolate import griddata

dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
TempA=dsTempA.THETAO
lat = np.array(TempA['LAT'].data)
depth = np.array(TempA['DEPTHT'].data)

glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv')
D1980s = glodap[glodap['Year']==1988]
D1990s = glodap[glodap['Year'].between(1990,2000, inclusive= False)]
D2000s = glodap[glodap['Year'].between(2000,2010, inclusive= False)]
D2010s = glodap[glodap['Year'].between(2010,2020, inclusive= False)]
datas = [D1980s,D1990s,D2000s,D2010s]
color = ['viridis','plasma','inferno','magma']

#for i in range(len(datas)):
#    data=datas[i]
#    x=data['Latitude'].values
#    y=data['Depth'].values
#    T=data['Temperature'].values
#    plt.subplot()
#    zi = griddata((x, y), T, (lat[None,:], depth[:,None]), method='linear')
#    CS = plt.contourf(lat, depth, zi, cmap=color[i])

    
x = D1980s['Latitude']
y = D1980s['Depth']
T1980s = D1980s['Temperature']

zi = griddata((x, y), T1980s, (lat[None,:], depth[:,None]), method='cubic', rescale=True)
CS = plt.contourf(lat, depth, zi, cmap='nipy_spectral', levels=30)
plt.colorbar()
plt.ylim(6000,0)