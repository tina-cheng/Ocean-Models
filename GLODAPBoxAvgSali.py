#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:51:58 2020

@author: Tina-CTH
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec
#%matplotlib inline
#%config InlineBackend.figure_format='retina'

import pandas as pd
import xarray as xr

glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv')

g_1990s = glodap[glodap['Year'].between(1990,2000, inclusive= False)]
g_2000s = glodap[glodap['Year'].between(2000,2010, inclusive= False)]
g_2010s = glodap[glodap['Year'].between(2010,2020, inclusive= False)]

between_latitudes = np.arange(-62.48,64.52,2)
for_dataframe = list(between_latitudes+1) #plotting it in the middle of the 2 points

d_100 = list([-100]*63)
d_500 = list([-500]*63)
d_1000 = list([-1000]*63)
d_2500 = list([-2500]*63)
d_4000 = list([-4000]*63)
d_6000 = list([-6000]*63)

temp_average_2010s = pd.DataFrame(for_dataframe[:-1], columns=['Latitude'])
temp_100_2010s = []
temp_500_2010s = []
temp_1000_2010s = []
temp_2500_2010s = []
temp_4000_2010s = []
temp_6000_2010s = []

#%%

for i in range(0, len(between_latitudes)-1):
    #print(between_latitudes[i])
    average_100 = g_2010s[(g_2010s['Depth'].between(0,100, inclusive= True))
                      &(g_2010s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Salinity'].mean()
    temp_100_2010s.append(average_100)
   
    average_500 = g_2010s[(g_2010s['Depth'].between(100.1,500, inclusive= True))
                      &(g_2010s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Salinity'].mean()
    temp_500_2010s.append(average_500)
   
    average_1000 = g_2010s[(g_2010s['Depth'].between(500.1,1000, inclusive= True))
                      &(g_2010s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Salinity'].mean()
    temp_1000_2010s.append(average_1000)
   
    average_2500 = g_2010s[(g_2010s['Depth'].between(1001.1,2500, inclusive= True))
                      &(g_2010s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Salinity'].mean()
    temp_2500_2010s.append(average_2500)
   
    average_4000 = g_2010s[(g_2010s['Depth'].between(2501.1,4000, inclusive= True))
                      &(g_2010s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Salinity'].mean()
    temp_4000_2010s.append(average_4000)
   
    average_6000 = g_2010s[(g_2010s['Depth'].between(4001.1,6010, inclusive= True))
                      &(g_2010s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Salinity'].mean()
    temp_6000_2010s.append(average_6000)
   

temp_average_2010s['temp_100'] = temp_100_2010s
temp_average_2010s['temp_500'] = temp_500_2010s
temp_average_2010s['temp_1000'] = temp_1000_2010s
temp_average_2010s['temp_2500'] = temp_2500_2010s
temp_average_2010s['temp_4000'] = temp_4000_2010s
temp_average_2010s['temp_6000'] = temp_6000_2010s

temp_average_2010s['depth_100'] = d_100
temp_average_2010s['depth_500'] = d_500
temp_average_2010s['depth_1000'] = d_1000
temp_average_2010s['depth_2500'] = d_2500
temp_average_2010s['depth_4000'] = d_4000
temp_average_2010s['depth_6000'] = d_6000


params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 20, # fontsize for x and y labels (was 10)
    'axes.titlesize': 20,
    'font.size': 20, # was 10
    'legend.fontsize': 20, # was 10
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'figure.figsize': [5, 5],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)
fig= plt.figure()
ax = plt.gca()
col_2010 = temp_average_2010s.columns

for i in range(1,7):
    x = temp_average_2010s[col_2010[0]]
    y = temp_average_2010s[col_2010[i+6]]
    c = temp_average_2010s[col_2010[i]]
    sc = plt.scatter(x=x, y=y, c=c, cmap='inferno')
    plt.title('2010s')
    if i ==1:
        cb = plt.colorbar(sc)
    plt.ylim(-6500,0); fig.show()

#%%
temp_average_2000s = pd.DataFrame(for_dataframe[:-1], columns=['Latitude'])
temp_100_2000s = []
temp_500_2000s = []
temp_1000_2000s = []
temp_2500_2000s = []
temp_4000_2000s = []
temp_6000_2000s = []

for i in range(0, len(between_latitudes)-1):
    #print(between_latitudes[i])
    average_100 = g_2000s[(g_2000s['Depth'].between(0,100, inclusive= True))
                      &(g_2000s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Salinity'].mean()
    temp_100_2000s.append(average_100)
   
    average_500 = g_2000s[(g_2000s['Depth'].between(100.1,500, inclusive= True))
                      &(g_2000s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_500_2000s.append(average_500)
   
    average_1000 = g_2000s[(g_2000s['Depth'].between(500.1,1000, inclusive= True))
                      &(g_2000s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_1000_2000s.append(average_1000)
   
    average_2500 = g_2000s[(g_2000s['Depth'].between(1001.1,2500, inclusive= True))
                      &(g_2000s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_2500_2000s.append(average_2500)
   
    average_4000 = g_2000s[(g_2000s['Depth'].between(2501.1,4000, inclusive= True))
                      &(g_2000s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_4000_2000s.append(average_4000)
   
    average_6000 = g_2000s[(g_2000s['Depth'].between(4001.1,6010, inclusive= True))
                      &(g_2000s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_6000_2000s.append(average_6000)
   
temp_average_2000s['temp_100'] = temp_100_2000s
temp_average_2000s['temp_500'] = temp_500_2000s
temp_average_2000s['temp_1000'] = temp_1000_2000s
temp_average_2000s['temp_2500'] = temp_2500_2000s
temp_average_2000s['temp_4000'] = temp_4000_2000s
temp_average_2000s['temp_6000'] = temp_6000_2000s

temp_average_2000s['depth_100'] = d_100
temp_average_2000s['depth_500'] = d_500
temp_average_2000s['depth_1000'] = d_1000
temp_average_2000s['depth_2500'] = d_2500
temp_average_2000s['depth_4000'] = d_4000
temp_average_2000s['depth_6000'] = d_6000

params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 20, # fontsize for x and y labels (was 10)
    'axes.titlesize': 20,
    'font.size': 20, # was 10
    'legend.fontsize': 20, # was 10
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'figure.figsize': [5, 5],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)
fig= plt.figure()
ax = plt.gca()
col_2000 = temp_average_2000s.columns
for i in range(1,7):
    x = temp_average_2000s[col_2000[0]]
    y = temp_average_2000s[col_2000[i+6]]
    c = temp_average_2000s[col_2000[i]]
    sc = plt.scatter(x=x, y=y, c=c, cmap='inferno', vmin=temp_average_2000s.temp_6000.min(),
                     vmax=temp_average_2000s.temp_100.max())
    plt.title('2000s')
    if i ==1:
        cb = plt.colorbar(sc)
    plt.ylim(-6500,0); fig.show()

#%%
    
temp_average_1990s = pd.DataFrame(for_dataframe[:-1], columns=['Latitude'])
temp_100_1990s = []
temp_500_1990s = []
temp_1000_1990s = []
temp_2500_1990s = []
temp_4000_1990s = []
temp_6000_1990s = []

for i in range(0, len(between_latitudes)-1):
    #print(between_latitudes[i])
    average_100 = g_1990s[(g_1990s['Depth'].between(0,100, inclusive= True))
                      &(g_1990s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_100_1990s.append(average_100)
   
    average_500 = g_1990s[(g_1990s['Depth'].between(100.1,500, inclusive= True))
                      &(g_1990s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_500_1990s.append(average_500)
   
    average_1000 = g_1990s[(g_1990s['Depth'].between(500.1,1000, inclusive= True))
                      &(g_1990s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_1000_1990s.append(average_1000)
   
    average_2500 = g_1990s[(g_1990s['Depth'].between(1001.1,2500, inclusive= True))
                      &(g_1990s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_2500_1990s.append(average_2500)
   
    average_4000 = g_1990s[(g_1990s['Depth'].between(2501.1,4000, inclusive= True))
                      &(g_1990s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_4000_1990s.append(average_4000)
   
    average_6000 = g_1990s[(g_1990s['Depth'].between(4001.1,6010, inclusive= True))
                      &(g_1990s['Latitude'].between(between_latitudes[i],between_latitudes[i+1],
                                                    inclusive = False))]['Temperature'].mean()
    temp_6000_1990s.append(average_6000)

temp_average_1990s['temp_100'] = temp_100_1990s
temp_average_1990s['temp_500'] = temp_500_1990s
temp_average_1990s['temp_1000'] = temp_1000_1990s
temp_average_1990s['temp_2500'] = temp_2500_1990s
temp_average_1990s['temp_4000'] = temp_4000_1990s
temp_average_1990s['temp_6000'] = temp_6000_1990s


temp_average_1990s['depth_100'] = d_100
temp_average_1990s['depth_500'] = d_500
temp_average_1990s['depth_1000'] = d_1000
temp_average_1990s['depth_2500'] = d_2500
temp_average_1990s['depth_4000'] = d_4000
temp_average_1990s['depth_6000'] = d_6000


params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 20, # fontsize for x and y labels (was 10)
    'axes.titlesize': 20,
    'font.size': 20, # was 10
    'legend.fontsize': 20, # was 10
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'figure.figsize': [5, 5],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)
col_1990 = temp_average_1990s.columns
matplotlib.rcParams.update(params)
fig= plt.figure()
ax = plt.gca()
for i in range(1,7):
    x = temp_average_1990s[col_1990[0]]
    y = temp_average_1990s[col_1990[i+6]]
    c = temp_average_1990s[col_1990[i]]
    sc = plt.scatter(x=x, y=y, c=c, cmap='inferno', vmin=temp_average_1990s.temp_6000.min(),
                     vmax=temp_average_1990s.temp_100.max())
    plt.title('1990s')
    if i ==1:
        cb = plt.colorbar(sc)
    plt.ylim(-6500,0); fig.show()